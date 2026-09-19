# NeetCode 150 tracker — working agreement

This folder tracks my NeetCode 150 progress. I solve problems on LeetCode
(shared premium account, so its own progress tracking is useless to me) and
file them here.

## The one thing to know

`progress.json` is the single source of truth. `README.md` is GENERATED from it.
Never hand-edit README.md — run `python tools/nc.py readme` instead.
Only problems I have actually solved appear in the README. Do not add rows for
unsolved problems, and do not create placeholder or stub files for problems I
have not done. The repo should only ever contain work I actually did.

## My main workflow

I will paste a problem name and my solution code. When I do:

1. Find the problem: `python tools/nc.py find <query>` (fuzzy matches title or slug).
2. Create the file: `python tools/nc.py new <slug>` — this writes
   `solutions/<NN-category>/<slug>.py` from the template with the right header.
   The category folder is created on demand.
3. Paste my code into that file, keeping the docstring header, and fill in:
   - `Pattern:` the technique (e.g. "two pointers on a sorted array")
   - `Time:` / `Space:` the real complexity of MY code, not the optimal one
   - the one-sentence idea, and "Where I got stuck" if I mentioned struggling
4. Add 2–3 cases to the `TESTS` list and run the file to confirm they pass.
5. Log it: `python tools/nc.py log <slug> -c <1-5> -m <minutes>`
   Add `--hint` if I said I looked at the solution. `-n "note"` for a note.
   This updates progress.json AND regenerates the README.
6. Commit with a message like `solve: two-sum (easy, 18m)`. Push if I ask.

If I do not give a confidence rating, ask me for one — do not guess it. It
drives the spaced-repetition schedule and a wrong value silently corrupts my
review queue.

## Reviewing my code

Tell me plainly when my solution is worse than it should be — wrong complexity,
an accidental O(n²) from slicing in a loop, a pattern that does not generalise.
Do not rewrite it into something I would not have written. If there is a better
approach, explain the idea and let me implement it. I am practising, not
shipping.

## The CLI

```
python tools/nc.py next              # next unsolved problem, scaffolds the file
python tools/nc.py next -c trees     # next one in a category
python tools/nc.py new <slug>        # scaffold a specific problem
python tools/nc.py log <slug> -c 3 -m 25 [--hint] [-n "note"]
python tools/nc.py review            # what is due for another pass today
python tools/nc.py stats             # progress and weak spots
python tools/nc.py find <query>      # search the 150
python tools/nc.py readme            # regenerate README.md
python tools/nc.py csv               # export progress.csv for my spreadsheet
```

Standard library only. No dependencies, no venv, no pip install.

## Layout

```
data/problems.json    the canonical 150 (metadata + links). Reference data — do not edit.
progress.json         source of truth for what I've solved. Edited via nc.py, not by hand.
solutions/NN-cat/     one file per solved problem. Created on demand.
tools/nc.py           the CLI
tools/templates/      python.tmpl and java.tmpl stubs
README.md             GENERATED
```

## Language

Python by default. Java only if I explicitly ask (`nc.py new <slug> -l java`).

## Rules of the grind (hold me to these)

- 30 minutes stuck, then read the solution, mark `--hint`, re-solve from blank
  a day or two later. Do not let me skip the re-solve.
- Never paste a solution in that I did not write or understand.
- Confidence ratings must be honest. If I claim a 5 on something that took me
  40 minutes and a hint, push back.
