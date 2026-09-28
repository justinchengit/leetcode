"""
Contains Duplicate  [Easy]
Arrays & Hashing

LeetCode: https://leetcode.com/problems/contains-duplicate/
NeetCode: https://neetcode.io/problems/duplicate-integer?list=neetcode150

Pattern: one pass with a "seen" set, checking membership before inserting
Time:   O(n)
Space:  O(n)

The idea in one sentence (write this AFTER you solve it — this is the part
you'll actually reread before an interview):
Walk the array once keeping every number I have already passed in a set, and
the first number that is already in the set is a duplicate.

Where I got stuck:
Nothing. Two things I took away: a set costs real extra space (O(n)) in
exchange for O(1) lookups, and the fact that a set silently drops duplicates
is fine here because the `in` check happens BEFORE the insert. Also: no `else`
needed after a `return` inside the loop, just dedent.
"""
from typing import List, Optional


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for number in nums:
            if (number in unique):
                return True
            unique.add(number)

        return False


# (args_tuple, expected)
TESTS = [
    (([1, 2, 3, 1],), True),
    (([1, 2, 3, 4],), False),
    (([],), False),
    (([7, 7],), True),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.hasDuplicate(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
    if not TESTS:
        print("No tests yet — add a couple of cases to TESTS.")
