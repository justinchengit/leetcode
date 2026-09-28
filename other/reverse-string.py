"""
Reverse String  [Easy]
LeetCode 344 — https://leetcode.com/problems/reverse-string/
Not part of NeetCode 150.

Pattern: two pointers swapping inward from both ends, in place
Time:   O(n)
Space:  O(1)

The idea in one sentence:
Swap the first and last characters, step both pointers inward, and stop when
they meet.

Where I got stuck:
Nothing. Note: the three-line temp swap is one line in Python,
`s[i], s[j] = s[j], s[i]`, because the right side is built before anything is
assigned. Also this returns None on purpose, the problem wants the list mutated
in place.
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            temp = s[j]
            s[j] = s[i]
            s[i] = temp

            i += 1
            j -= 1


# (input_list, expected_after_mutation)
TESTS = [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    (["a", "b"], ["b", "a"]),
    (["a"], ["a"]),
    ([], []),
]

if __name__ == "__main__":
    s = Solution()
    for i, (arg, want) in enumerate(TESTS, 1):
        buf = list(arg)
        ret = s.reverseString(buf)
        ok = buf == want and ret is None
        print(f"{'PASS' if ok else 'FAIL'} #{i}  got={buf!r} want={want!r} returned={ret!r}")
