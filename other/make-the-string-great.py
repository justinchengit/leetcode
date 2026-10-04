"""
Make The String Great  [Easy]
LeetCode 1544 — https://leetcode.com/problems/make-the-string-great/
Study guide: Stacks and Queues > String problems
Not part of NeetCode 150.

Pattern: stack, cancel the top when the incoming character is its case-flip
Time:   O(n)
Space:  O(n)

The idea in one sentence:
Push characters one at a time, and whenever the new one is the same letter in
the opposite case as the top of the stack, drop both instead of pushing.

Why a stack and not a scan: removing a bad pair can create a NEW bad pair out
of its neighbours ("abBA" collapses to nothing), and the stack re-checks the
exposed top for free. A single left-to-right pass without one would miss that.

Optimal: each character is pushed and popped at most once.

Note: swapcase() is the clearest way to test it, but not the only one.
`a.lower() == b.lower() and a != b` works, and so does
`abs(ord(a) - ord(b)) == 32`, since that is the ASCII gap between the cases.

Also `for c in range(len(s))` then `s[c]` can be `for c in s`, and the name `c`
reads like a character rather than an index.
"""


class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for c in range(len(s)):
            if stack and s[c] == stack[-1].swapcase():
                stack.pop()
            else:
                stack.append(s[c])

        return "".join(stack)


# (args_tuple, expected)
TESTS = [
    (("leEeetcode",), "leetcode"),
    (("abBAcC",), ""),          # cascading: removing bB exposes aA, then cC
    (("s",), "s"),
    (("",), ""),
    (("aA",), ""),
    (("aa",), "aa"),            # same case, not a bad pair
    (("Pp",), ""),
    (("mMmM",), ""),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.makeGood(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
