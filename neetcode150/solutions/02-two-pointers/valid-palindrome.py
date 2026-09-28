"""
Valid Palindrome  [Easy]
Two Pointers

LeetCode: https://leetcode.com/problems/valid-palindrome/
NeetCode: https://neetcode.io/problems/is-palindrome?list=neetcode150

Pattern: two pointers walking inward from both ends, skipping junk characters
Time:   O(n)
Space:  O(1)   no cleaned copy of the string is ever built

The idea in one sentence (write this AFTER you solve it — this is the part
you'll actually reread before an interview):
Walk one index in from the left and one in from the right, skip anything that
is not alphanumeric, and the moment the two characters disagree it is not a
palindrome.

Where I got stuck:
Nothing. Learned that "two pointers" are just two indexes, not pointers in the
C sense, .lower() is a method so it needs the parentheses, and .isalnum() tests
the CONTENT of a string (every character is a letter or digit) rather than a
type.

Skipping in place is what keeps this O(1) space: building a cleaned copy of the
string first would work and be just as fast, but it costs O(n) memory.
"""
from typing import List, Optional


class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l < r:
            if s[l].isalnum() == False:
                l += 1
                continue
            if s[r].isalnum() == False:
                r -= 1
                continue
            if s[r].lower() != s[l].lower():
                return False
            r -= 1
            l += 1

        return True


# (args_tuple, expected)
TESTS = [
    (("A man, a plan, a canal: Panama",), True),
    (("race a car",), False),
    (("",), True),
    ((" ",), True),          # all junk, pointers cross immediately
    (("0P",), False),        # digit vs letter, catches ASCII-arithmetic bugs
    (("ab_a",), True),       # junk in the middle
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.isPalindrome(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
    if not TESTS:
        print("No tests yet — add a couple of cases to TESTS.")
