"""
Best Time to Buy And Sell Stock  [Easy]
Sliding Window

LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
NeetCode: https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150

Pattern: two pointers, but the left one rewinds to the cheapest day seen so far
Time:   O(n^2) worst case   (measured: 499,500 inner steps on a rising list of 1000)
Space:  O(1)

The idea in one sentence (write this AFTER you solve it — this is the part
you'll actually reread before an interview):
For every day, compare selling that day against every earlier buy day still in
range, while separately remembering the cheapest day so the left pointer can
rewind to it.

Where I got stuck:
The answer is right but the shape is wrong. Resetting `l = smallest_index`
means the left side rescans instead of advancing, so on a rising list the
cheapest day stays index 0 and every day re-walks the whole prefix. Measured:
rising input costs n(n-1)/2 inner steps, falling input costs about 2n.

TODO re-solve: only two things actually matter, the cheapest price seen so far
and the best profit so far, so one pass with two variables and no inner loop
gets this to O(n). I do not need the index of the cheapest day at all, only
its price.
"""
from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # array prices of ith day
        # don't want to make negative money - make sure the difference ain't negative

        l = 0
        profit = 0
        smallest_price = float("inf")
        smallest_index = 0

        for r, val in enumerate(prices):

            while l != r:
                profit = max(profit, val - prices[l])
                if smallest_price - float(prices[l]) > 0:
                    smallest_price = prices[l]
                    smallest_index = l
                l += 1

            l = smallest_index

        return profit


# (args_tuple, expected)
TESTS = [
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),     # only losses, never buy
    (([1, 2],), 1),
    (([5],), 0),
    (([],), 0),
    (([2, 4, 1],), 2),           # best sell happens before the cheapest day
    (([3, 2, 6, 5, 0, 3],), 4),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.maxProfit(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
    if not TESTS:
        print("No tests yet — add a couple of cases to TESTS.")
