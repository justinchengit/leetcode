"""
Valid Anagram  [Easy]
Arrays & Hashing

LeetCode: https://leetcode.com/problems/valid-anagram/
NeetCode: https://neetcode.io/problems/is-anagram?list=neetcode150

Pattern: character counts in a dict, add walking s, subtract walking t
Time:   O(n)
Space:  O(1)   at most 26 keys, bounded by the alphabet not the input

The idea in one sentence (write this AFTER you solve it — this is the part
you'll actually reread before an interview):
Anagrams have identical letter counts, so tally s in a dict, undo the tally
with t, and if the lengths matched then every count ends at zero.

Where I got stuck:
First pass was the sort version (O(n log n), kept below). Coming back for the
counting version, the real errors were mine on Python, not the algorithm:
`len(s)` is a builtin not a method, `d[c] = d.get(c, 0) + 1` needs the
assignment or the new count is discarded, and you cannot bail out from inside
an argument (`d.get(c, return False)` is a SyntaxError), so the missing-key
check has to be its own `if` before the decrement. Also `-=` to write the
decrement back, and the values are ints so `all(v == 0 ...)` can be returned
directly.

Length check first is what makes the final all-zeros test sound: equal lengths
plus every subtraction matched by an addition means nothing can be left over.
"""
from typing import List, Optional


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        if len(s) != len(t):
            return False

        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            if c not in d:
                return False
            d[c] -= 1

        return all(v == 0 for v in d.values())


class FirstPass:
    """O(n log n) sort version, my first attempt. Kept for the contrast."""

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# (args_tuple, expected)
TESTS = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("", ""), True),
    (("a", "ab"), False),
    (("aacc", "ccac"), False),   # same letters, different counts
    (("aab", "abb"), False),     # count goes negative, caught by the all()
]

if __name__ == "__main__":
    s = Solution()
    old = FirstPass()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.isAnagram(*args)
        also = old.isAnagram(*args)
        flag = "PASS" if got == want and also == want else "FAIL"
        print(f"{flag} #{i}  got={got!r} sort={also!r} want={want!r}")
    if not TESTS:
        print("No tests yet — add a couple of cases to TESTS.")
