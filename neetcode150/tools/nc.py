#!/usr/bin/env python3
"""
nc - NeetCode 150 tracker. Standard library only, no pip install.

    python tools/nc.py next              # next unsolved problem + make the stub file
    python tools/nc.py log two-sum -c 4 -m 18
    python tools/nc.py review            # what's due today
    python tools/nc.py stats
    python tools/nc.py readme            # regenerate README.md
    python tools/nc.py csv               # export for the spreadsheet

Single source of truth is progress.json (git-tracked). README.md is generated;
never edit it by hand.
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = json.loads((ROOT / "data" / "problems.json").read_text())
PROGRESS_PATH = ROOT / "progress.json"
TEMPLATES = ROOT / "tools" / "templates"

# Days until next review, indexed by confidence 1-5. Repeat successes stretch it.
INTERVALS = {1: 1, 2: 3, 3: 7, 4: 16, 5: 35}
EXT = {"python": "py", "java": "java"}
TODAY = dt.date.today()


# ---------------------------------------------------------------- data access


def load_progress():
    if PROGRESS_PATH.exists():
        return json.loads(PROGRESS_PATH.read_text())
    return {}


def save_progress(p):
    PROGRESS_PATH.write_text(json.dumps(p, indent=2, sort_keys=True) + "\n")


def find(query):
    """Match a problem by exact slug, then by fuzzy title/slug substring."""
    q = query.lower().strip()
    for p in PROBLEMS:
        if p["slug"] == q:
            return p
    hits = [p for p in PROBLEMS if q in p["slug"] or q in p["title"].lower()]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        sys.exit(f"No problem matches {query!r}. Try: nc.py find {q}")
    sys.exit(
        "Ambiguous - did you mean one of:\n"
        + "\n".join(f"  {h['slug']}  ({h['title']})" for h in hits[:10])
    )


def rec(progress, slug):
    return progress.get(slug, {})


def is_solved(progress, slug):
    return bool(rec(progress, slug).get("solved_on"))


def next_review(r):
    if not r.get("last_review"):
        return None
    conf = r.get("confidence", 3)
    reps = max(1, r.get("reviews", 1))
    # each clean repeat stretches the interval, capped so nothing vanishes for a year
    days = min(INTERVALS.get(conf, 7) * (1.7 ** (reps - 1)), 180)
    return dt.date.fromisoformat(r["last_review"]) + dt.timedelta(days=round(days))


def due(progress, slug):
    """True when a solved problem is ready for another pass."""
    r = rec(progress, slug)
    nr = next_review(r)
    return bool(nr and nr <= TODAY)


def solution_path(p, lang):
    return ROOT / "solutions" / p["dir"] / f"{p['slug']}.{EXT[lang]}"


def bar(done, total, width=22):
    filled = 0 if not total else round(width * done / total)
    return "█" * filled + "░" * (width - filled)


# ------------------------------------------------------------------ commands


def make_stub(p, lang, quiet=False):
    path = solution_path(p, lang)
    if path.exists():
        if not quiet:
            print(f"  exists: {path.relative_to(ROOT)}")
        return path
    tmpl = (TEMPLATES / f"{lang}.tmpl").read_text()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        tmpl.format(
            title=p["title"],
            difficulty=p["difficulty"],
            category=p["category"],
            leetcode=p["leetcode"],
            neetcode=p["neetcode"],
            classname="".join(w for w in p["title"].title() if w.isalnum()),
        )
    )
    if not quiet:
        print(f"  created: {path.relative_to(ROOT)}")
    return path


def cmd_next(args):
    progress = load_progress()
    pool = PROBLEMS
    if args.category:
        c = args.category.lower()
        pool = [p for p in PROBLEMS if c in p["category"].lower() or c in p["dir"]]
    if args.difficulty:
        pool = [p for p in pool if p["difficulty"].lower() == args.difficulty.lower()]

    todo = [p for p in pool if not is_solved(progress, p["slug"])]
    if not todo:
        print("Nothing left in that filter. Try `nc.py review`.")
        return
    p = todo[0]
    n = len([x for x in PROBLEMS if is_solved(progress, x["slug"])])
    print(f"\n#{p['id']}/150  {p['title']}  [{p['difficulty']}]")
    print(f"  {p['category']}")
    print(f"  LeetCode: {p['leetcode']}")
    print(f"  NeetCode: {p['neetcode']}")
    make_stub(p, args.lang)
    print(f"\n  Solved so far: {n}/150   {bar(n, 150)}")
    print(f"  When you're done:  python tools/nc.py log {p['slug']} -c 3 -m 25\n")


def cmd_new(args):
    for q in args.query:
        p = find(q)
        print(f"{p['title']} [{p['difficulty']}]")
        make_stub(p, args.lang)


def cmd_log(args):
    progress = load_progress()
    p = find(args.query)
    slug = p["slug"]
    r = progress.setdefault(slug, {})

    r["attempts"] = r.get("attempts", 0) + 1
    r["reviews"] = r.get("reviews", 0) + 1
    if not r.get("solved_on"):
        r["solved_on"] = TODAY.isoformat()
        r["reviews"] = 1
    r["last_review"] = TODAY.isoformat()
    r["confidence"] = args.confidence
    if args.minutes:
        r["minutes"] = args.minutes
        r.setdefault("minutes_history", []).append(args.minutes)
    if args.hint:
        r["needed_hint"] = True
    if args.note:
        r["note"] = args.note
    # A weak pass resets the streak so the interval shrinks back down.
    if args.confidence <= 2:
        r["reviews"] = 1

    save_progress(progress)
    nr = next_review(r)
    n = len([x for x in PROBLEMS if is_solved(progress, x["slug"])])
    print(f"Logged {p['title']}  confidence={args.confidence}"
          + (f"  {args.minutes}min" if args.minutes else ""))
    print(f"  Next review: {nr} ({(nr - TODAY).days}d)")
    print(f"  Progress: {n}/150  {bar(n, 150)}")
    if not any(solution_path(p, lang).exists() for lang in EXT):
        print(f"  note: no solution file yet — `python tools/nc.py new {slug}` to create one")
    if not args.no_readme:
        write_readme(progress)
        print("  README.md updated")


def cmd_review(args):
    progress = load_progress()
    rows = []
    for p in PROBLEMS:
        if due(progress, p["slug"]):
            r = rec(progress, p["slug"])
            nr = next_review(r)
            rows.append((p, r, (TODAY - nr).days))
    if not rows:
        upcoming = sorted(
            ((next_review(rec(progress, p["slug"])), p) for p in PROBLEMS
             if is_solved(progress, p["slug"])),
            key=lambda t: t[0],
        )
        print("Nothing due today.")
        if upcoming:
            d, p = upcoming[0]
            print(f"  Next up: {p['title']} on {d} ({(d - TODAY).days}d)")
        return
    rows.sort(key=lambda t: (-t[2], t[1].get("confidence", 3)))
    print(f"\n{len(rows)} due for review (weakest first):\n")
    for p, r, over in rows[: args.limit]:
        flag = "!" if r.get("confidence", 3) <= 2 else " "
        print(f" {flag} {p['title']:<44} conf={r.get('confidence','?')} "
              f"{over}d overdue  {p['leetcode']}")
    print()


def cmd_find(args):
    q = args.query.lower()
    progress = load_progress()
    for p in PROBLEMS:
        if q in p["slug"] or q in p["title"].lower() or q in p["category"].lower():
            mark = "x" if is_solved(progress, p["slug"]) else " "
            print(f"[{mark}] #{p['id']:>3} {p['slug']:<44} {p['difficulty']:<6} {p['category']}")


def cmd_stats(args):
    progress = load_progress()
    solved = [p for p in PROBLEMS if is_solved(progress, p["slug"])]
    print(f"\nNeetCode 150 - {len(solved)}/150  {bar(len(solved), 150)}\n")

    for d in ("Easy", "Medium", "Hard"):
        tot = [p for p in PROBLEMS if p["difficulty"] == d]
        s = [p for p in solved if p["difficulty"] == d]
        print(f"  {d:<7} {len(s):>3}/{len(tot):<4} {bar(len(s), len(tot), 16)}")

    print()
    seen = []
    for p in PROBLEMS:
        if p["category"] not in seen:
            seen.append(p["category"])
    for c in seen:
        tot = [p for p in PROBLEMS if p["category"] == c]
        s = [p for p in solved if p["category"] == c]
        print(f"  {c:<26} {len(s):>2}/{len(tot):<3} {bar(len(s), len(tot), 16)}")

    mins = [r["minutes"] for r in progress.values() if r.get("minutes")]
    confs = [r["confidence"] for r in progress.values() if r.get("confidence")]
    hints = [r for r in progress.values() if r.get("needed_hint")]
    n_due = len([p for p in PROBLEMS if due(progress, p["slug"])])
    print()
    if mins:
        print(f"  median time   {sorted(mins)[len(mins)//2]} min")
    if confs:
        print(f"  avg confidence {sum(confs)/len(confs):.1f}/5")
    if solved:
        print(f"  needed a hint  {len(hints)}/{len(solved)}")
    print(f"  due for review {n_due}")
    weak = sorted(
        [(r.get("confidence", 5), s) for s, r in progress.items() if r.get("confidence", 5) <= 2]
    )
    if weak:
        print("\n  shakiest: " + ", ".join(s for _, s in weak[:6]))
    print()


def cmd_csv(args):
    progress = load_progress()
    out = ROOT / "progress.csv"
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["#", "Category", "Problem", "Difficulty", "LeetCode", "NeetCode",
                    "Status", "Attempts", "First Solved", "Last Review", "Confidence",
                    "Next Review", "Minutes", "Notes"])
        for p in PROBLEMS:
            r = rec(progress, p["slug"])
            status = ("Solved" if r.get("solved_on")
                      else "Attempted" if r.get("attempts") else "Not started")
            nr = next_review(r)
            w.writerow([p["id"], p["category"], p["title"], p["difficulty"],
                        p["leetcode"], p["neetcode"], status, r.get("attempts", ""),
                        r.get("solved_on", ""), r.get("last_review", ""),
                        r.get("confidence", ""), nr or "", r.get("minutes", ""),
                        r.get("note", "")])
    print(f"Wrote {out.relative_to(ROOT)} - paste into the Tracker sheet.")


# ------------------------------------------------------------------- readme


def write_readme(progress=None):
    progress = load_progress() if progress is None else progress
    solved = [p for p in PROBLEMS if is_solved(progress, p["slug"])]
    n = len(solved)
    L = []
    L.append("# NeetCode 150\n")
    L.append(f"**{n} / 150 solved**\n")
    L.append(f"`{bar(n, 150, 40)}` {n/150*100:.0f}%\n")

    L.append("| Difficulty | Progress |")
    L.append("|---|---|")
    for d in ("Easy", "Medium", "Hard"):
        tot = len([p for p in PROBLEMS if p["difficulty"] == d])
        s = len([p for p in solved if p["difficulty"] == d])
        L.append(f"| {d} | `{bar(s, tot, 18)}` {s}/{tot} |")
    L.append("")

    L.append("""<details>
<summary><b>How I use this</b></summary>

```bash
python tools/nc.py next            # next unsolved problem + creates the stub file
python tools/nc.py next -c trees   # next one in a category
python tools/nc.py log two-sum -c 3 -m 25      # after solving: confidence 1-5, minutes
python tools/nc.py log two-sum -c 1 --hint     # --hint = I looked at the answer
python tools/nc.py review          # what's due for a second pass today
python tools/nc.py stats           # where I'm weak
python tools/nc.py csv             # export for the spreadsheet
```

**Confidence** is the whole point of the tracker: `1` no idea, `3` got there with
effort, `5` instant. It sets when the problem comes back — a 1 returns tomorrow, a
5 in five weeks. Rate honestly; rating yourself generous just means you meet the
problem again for the first time in the interview.

Rules I'm holding myself to: 30 minutes stuck, then read the solution, mark
`--hint`, and re-solve it from blank in a day or two. Never copy-paste a solution
in. Fill in the one-sentence summary at the top of each file after solving —
that's the part worth rereading later.

</details>
""")

    due_now = [p for p in PROBLEMS if due(progress, p["slug"])]
    if due_now:
        L.append(f"### Due for review ({len(due_now)})\n")
        L.append(", ".join(f"[{p['title']}]({p['leetcode']})" for p in due_now[:20]))
        L.append("")

    cats = []
    for p in PROBLEMS:
        if p["category"] not in cats:
            cats.append(p["category"])

    L.append("## Progress by category\n")
    L.append("| Category | Solved | |")
    L.append("|---|---|---|")
    for c in cats:
        tot = len([p for p in PROBLEMS if p["category"] == c])
        s = len([p for p in solved if p["category"] == c])
        L.append(f"| {c} | {s}/{tot} | `{bar(s, tot, 14)}` |")
    L.append("")

    L.append("## Solved\n")
    if not solved:
        L.append("_Nothing yet. `python tools/nc.py next` to start._\n")
    for c in cats:
        group = [p for p in PROBLEMS if p["category"] == c
                 and is_solved(progress, p["slug"])]
        if not group:                      # only categories you've actually touched
            continue
        total = len([p for p in PROBLEMS if p["category"] == c])
        L.append(f"### {c} &nbsp; {len(group)}/{total}\n")
        L.append("| # | Problem | Difficulty | Solution | Conf | Last reviewed | Links |")
        L.append("|---|---|---|---|---|---|---|")
        for p in group:
            r = rec(progress, p["slug"])
            sol = ""
            for lang, ext in EXT.items():
                f = solution_path(p, lang)
                if f.exists():
                    sol += f"[{ext}]({f.relative_to(ROOT).as_posix()}) "
            L.append(
                f"| {p['id']} | {p['title']} | {p['difficulty']} | {sol.strip() or '—'} "
                f"| {r.get('confidence','')} | {r.get('last_review','')} "
                f"| [LC]({p['leetcode']}) · [NC]({p['neetcode']}) |"
            )
        L.append("")

    L.append("---\n")
    L.append("<sub>Generated by `tools/nc.py readme` on "
             f"{TODAY.isoformat()}. Do not edit by hand.</sub>")
    (ROOT / "README.md").write_text("\n".join(L) + "\n")


def cmd_readme(args):
    write_readme()
    print("README.md regenerated.")


# --------------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(prog="nc", description="NeetCode 150 tracker")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_next = sub.add_parser("next", help="next unsolved problem, and scaffold it")
    p_next.add_argument("-c", "--category")
    p_next.add_argument("-d", "--difficulty", choices=["easy", "medium", "hard"])
    p_next.add_argument("-l", "--lang", default="python", choices=list(EXT))
    p_next.set_defaults(func=cmd_next)

    p_new = sub.add_parser("new", help="scaffold specific problems")
    p_new.add_argument("query", nargs="+")
    p_new.add_argument("-l", "--lang", default="python", choices=list(EXT))
    p_new.set_defaults(func=cmd_new)

    p_log = sub.add_parser("log", help="record an attempt")
    p_log.add_argument("query")
    p_log.add_argument("-c", "--confidence", type=int, choices=[1, 2, 3, 4, 5], required=True,
                       help="1=no idea, 3=got there with effort, 5=instant")
    p_log.add_argument("-m", "--minutes", type=int)
    p_log.add_argument("--hint", action="store_true", help="looked at the solution")
    p_log.add_argument("-n", "--note")
    p_log.add_argument("--no-readme", action="store_true")
    p_log.set_defaults(func=cmd_log)

    p_rev = sub.add_parser("review", help="what's due today")
    p_rev.add_argument("--limit", type=int, default=15)
    p_rev.set_defaults(func=cmd_review)

    p_find = sub.add_parser("find", help="search the list")
    p_find.add_argument("query")
    p_find.set_defaults(func=cmd_find)

    sub.add_parser("stats", help="progress breakdown").set_defaults(func=cmd_stats)
    sub.add_parser("readme", help="regenerate README.md").set_defaults(func=cmd_readme)
    sub.add_parser("csv", help="export progress.csv for the spreadsheet").set_defaults(func=cmd_csv)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
