"""
Missing Number  [Easy]
Bit Manipulation

LeetCode: https://leetcode.com/problems/missing-number/
NeetCode: https://neetcode.io/problems/missing-number?list=neetcode150
Study guide: Hashing > Checking for existence

Pattern: set for O(1) membership, then scan the full range 0..n
Time:   O(n)
Space:  O(n)

The idea in one sentence:
The array holds n of the n+1 values 0 through n, so put them in a set and walk
0..n to find the one that is not there.

Where I got stuck:
Nothing on the code. Learned that range(0, n+1) is what covers 0 through n
inclusive, since range stops short of its upper bound.

Corrections to what I first wrote in my notes:
  - This is NOT O(1). The set holds n values, so it is O(n) time AND O(n) space.
  - The math shortcut is sum(0..n) = n*(n+1)/2, not n*(n-1)/2, and it is a SUM,
    not an average. Subtract the sum of nums from it and the difference is the
    missing value.
  - That shortcut saves SPACE, not time: O(1) space instead of O(n), but still
    O(n) time, because every element has to be read at least once. O(n) time is
    the floor for this problem, so no approach beats it.
  - XOR is the third option and also O(1) space: XOR every index 0..n together
    with every element, and the pairs cancel, leaving the missing value. That is
    why NeetCode files this under Bit Manipulation.
"""
from typing import List, Optional


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        my_set = set()
        n = len(nums)

        for i in nums:
            my_set.add(i)

        for i in range(0, n+1):
            if i not in my_set:
                return i


# (args_tuple, expected)
TESTS = [
    (([3, 0, 1],), 2),
    (([0, 1],), 2),          # missing value is n itself
    (([1],), 0),             # missing value is 0
    (([0],), 1),
    (([9, 6, 4, 2, 3, 5, 7, 0, 1],), 8),
    (([0, 1, 2, 3, 5],), 4),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.missingNumber(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
