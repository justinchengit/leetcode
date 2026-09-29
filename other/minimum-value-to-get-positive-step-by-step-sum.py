"""
Minimum Value to Get Positive Step by Step Sum  [Easy]
LeetCode 1413 — https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
Study guide: Arrays and Strings > Prefix sum
Not part of NeetCode 150.

Pattern: prefix sum, then solve an inequality against its minimum
Time:   O(n)
Space:  O(n)   (only O(1) is actually needed, see below)

The idea in one sentence:
The start value has to keep every running total at 1 or above, so it only has
to survive the single worst dip: startValue >= 1 - min(prefix).

The algebra, which is the whole problem:
  need:  startValue + prefix[i] >= 1   for every i
  so:    startValue >= 1 - prefix[i]   for every i
  so:    startValue >= 1 - min(prefix)
  and    startValue >= 1               because it must be positive
  hence  answer = max(1 - least, 1)

Where I got stuck:
Forgot the second constraint. If the running sum never dips, 1 - least comes
out negative or zero, and a negative start value is not allowed. The max()
against 1 is what covers it.

Note for next time:
The prefix ARRAY is unnecessary here. Nothing ever looks back at an earlier
prefix, only at the running minimum, so a single running total and a single
`least` do the job in O(1) space. Also `sum` shadows the builtin, name it
`total`. And the `if i == 0` branch disappears if the running total starts at 0.
"""


class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = [0] * len(nums)
        least = float('inf')

        for i in range(len(nums)):
            if i == 0:
                sum[i] = nums[i]
                if sum[i] < least:
                    least = sum[i]
            else:
                sum[i] = sum[i-1] + nums[i]
                if sum[i] < least:
                    least = sum[i]

        return max(1-least, 1)


# (args_tuple, expected)
TESTS = [
    (([-3, 2, -3, 4, 2],), 5),
    (([1, 2],), 1),          # never dips, so the max() against 1 carries it
    (([1, -2, -3],), 5),
    (([-1],), 2),
    (([0],), 1),
    (([2, 3, 5],), 1),
    (([-5, -5, -5],), 16),   # worst dip is the very last prefix
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.minStartValue(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
