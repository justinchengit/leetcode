"""
Running Sum of 1d Array  [Easy]
LeetCode 1480 — https://leetcode.com/problems/running-sum-of-1d-array/
Study guide: Arrays and Strings > Prefix sum
Not part of NeetCode 150.

Pattern: prefix sum, each slot is the previous slot plus the current element
Time:   O(n)
Space:  O(n)   for the output (O(1) extra if written in place)

The idea in one sentence:
Each running total is just the one before it plus the current element, so one
pass builds the whole array.

Note for next time:
The `if i == 0` branch is avoidable. Keep a running total starting at 0 and add
to it each step, and the first element stops being special. Same trick as
starting a window empty: pick the representation where the base case is
expressible and it stops being a case.

This problem asks for the array, so O(n) space is required. If it had only
asked for lookups, the array could be written into nums itself for O(1) extra.
"""


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = [0] * (len(nums))

        for i in range(len(nums)):
            if i == 0:
                running_sum[i] = nums[i]
            else:
                running_sum[i] = running_sum[i-1] + nums[i]

        return running_sum


# (args_tuple, expected)
TESTS = [
    (([1, 2, 3, 4],), [1, 3, 6, 10]),
    (([1, 1, 1, 1, 1],), [1, 2, 3, 4, 5]),
    (([3, 1, 2, 10, 1],), [3, 4, 6, 16, 17]),
    (([-1, -2, -3],), [-1, -3, -6]),
    (([5],), [5]),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.runningSum(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
