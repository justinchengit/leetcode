"""
Next Greater Element I  [Easy]
LeetCode 496 — https://leetcode.com/problems/next-greater-element-i/
Study guide: Stacks and Queues > Monotonic stack
Not part of NeetCode 150.

Pattern: monotonic decreasing stack over nums2, answers resolved on the pop
Time:   O(n + m)
Space:  O(n)

The idea in one sentence:
Walk nums2 keeping a stack of values still waiting for a bigger neighbour, and
when a bigger value arrives it is the answer for everything it can pop.

Optimal: every value in nums2 is pushed once and popped at most once, so the
inner while loop is amortized O(1) per element despite looking nested. The
lookups for nums1 are O(1) each. You cannot do better than reading both arrays.

Why the stack stays sorted: anything smaller than the incoming value gets
popped before the push, so the stack is always decreasing from bottom to top.
That is the invariant that makes "the next bigger value" resolvable in one pass.

Note: `dict` shadows the builtin, same as `sum` and `map` earlier. Call it
`next_greater`. Also `dict[stack[-1]] = num; stack.pop()` can be
`next_greater[stack.pop()] = num`.
"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # find the next largest element for each element in nums1, sourcing them from nums2

        stack = []
        dict = {}
        ans = []

        for num in nums2:
            while stack and num > stack[-1]:
                dict[stack[-1]] = num
                stack.pop()
            stack.append(num)

        for i in nums1:
            if i in dict:
                ans.append(dict[i])
            else:
                ans.append(-1)

        return ans


# (args_tuple, expected)
TESTS = [
    (([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1]),
    (([2, 4], [1, 2, 3, 4]), [3, -1]),
    (([1], [1]), [-1]),
    (([5, 3], [5, 4, 3, 2, 1]), [-1, -1]),   # strictly decreasing, nothing resolves
    (([1, 2, 3], [1, 2, 3]), [2, 3, -1]),    # strictly increasing
    (([3], [1, 3, 2, 4]), [4]),              # answer is not the adjacent value
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.nextGreaterElement(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
