"""
Squares of a Sorted Array  [Easy]
LeetCode 977 — https://leetcode.com/problems/squares-of-a-sorted-array/
Not part of NeetCode 150.

Pattern: two pointers at both ends, write the result back to front
Time:   O(n)
Space:  O(n)   for the output array

The idea in one sentence:
The largest square has to come from one of the two ends because the input is
sorted by value but not by magnitude, so compare the absolute values at each
end and drop the bigger one into the last unfilled slot.

Where I got stuck:
Nothing, but the thing to remember: you need a separate array to write into.
Squaring in place would overwrite values you have not read yet.
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # find an O(n) solution:
        # thought about it - seems like i'll take a pointer to the first, then a pointer to the second one

        j = 0
        k = len(nums) - 1

        res = [0] * len(nums)

        for i in range(len(nums) - 1, - 1, -1):
            if abs(nums[k]) > abs(nums[j]):
                res[i] = nums[k] * nums[k]
                k -= 1
            else:
                res[i] = nums[j] * nums[j]
                j += 1

        return res


# (args_tuple, expected)
TESTS = [
    (([-4, -1, 0, 3, 10],), [0, 1, 9, 16, 100]),
    (([-7, -3, 2, 3, 11],), [4, 9, 9, 49, 121]),
    (([-5, -3, -1],), [1, 9, 25]),      # all negative, reversed order
    (([1, 2, 3],), [1, 4, 9]),          # all positive, already sorted
    (([-2, -2, 2, 2],), [4, 4, 4, 4]),  # ties on both sides
    (([1],), [1]),
    (([],), []),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.sortedSquares(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
