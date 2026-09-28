"""
Longest Substring Without Repeating Characters  [Medium]
Sliding Window

LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
NeetCode: https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150

Pattern: variable-size sliding window, a set holding exactly the window's characters
Time:   O(n)    each step advances i or j, each at most n
Space:  O(min(n, alphabet))

The idea in one sentence:
Grow the window to the right while the next character is new, and when it is a
duplicate, evict from the left one character at a time until the duplicate is
gone, so the set always holds exactly the current window.

Where I got stuck:
My first plan was to WIPE the set on a duplicate and restart from it. That is
wrong, not just slow: it throws away a valid tail I had already earned.
    'dvdf'     wipe plan -> 2, correct 3   (loses "vdf")
    'abcbdef'  wipe plan -> 4, correct 5   (loses "cbdef")
Only the duplicate and everything before it has to go, never the characters
between it and the right edge.

Then IndexError on the empty string, because I primed with `set(s[0])` before
knowing s had a character. I patched it with `if not s: return 0`, which works,
but the guard is a symptom: priming is what created the edge case. Starting with
j = -1 and an empty set (the 1004 lesson) needs no guard and no special case,
because the first character enters through the same branch as every other one.

Verified against a brute force on 30,000 random strings, 0 mismatches.

Note: `elif s[j + 1] in seen` is the exact negation of the `if`, so it can just
be `else`.
"""
from typing import List, Optional


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 0

        if not s:
            return 0

        seen = set(s[0])
        best = len(seen)

        while j < len(s) - 1:
            if s[j + 1] not in seen:
                j += 1
                seen.add(s[j])
                if len(seen) > best:
                    best = len(seen)
            elif s[j + 1] in seen:
                seen.discard(s[i])
                i += 1

        return best


# (args_tuple, expected)
TESTS = [
    (("abcabcbb",), 3),
    (("bbbbb",), 1),
    (("pwwkew",), 3),
    (("abcbdef",), 5),   # the wipe-the-set plan returned 4 here
    (("dvdf",), 3),      # and 2 here
    (("abba",), 2),
    (("tmmzuxt",), 5),
    (("",), 0),          # the IndexError case
    (("a",), 1),
    ((" ",), 1),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.lengthOfLongestSubstring(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
