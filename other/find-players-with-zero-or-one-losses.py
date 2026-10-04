"""
Find Players With Zero or One Losses  [Medium]
LeetCode 2225 — https://leetcode.com/problems/find-players-with-zero-or-one-losses/
Study guide: Hashing > Counting
Not part of NeetCode 150.

Pattern: set of winners plus a loss-count map, then filter each group
Time:   O(n log n)   the two sorts dominate, and sorted output is required
Space:  O(n)

The idea in one sentence:
Count losses per player while collecting everyone who ever won, then the
zero-loss group is the winners with no entry in the loss map and the one-loss
group is every key whose count is exactly 1.

This is optimal: the answer must come back sorted, so O(n log n) is the floor
unless you exploit the bounded player id (<= 10^5) to counting-sort in
O(n + maxId), which is not worth it.

Note: `if cond: continue else: append` reads better as
`if losses.get(i, 0) == 0: append`.
"""


class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """

        answer = [[], []]

        winner = set()
        losses = {}

        for i in matches:
            winner.add(i[0])
            losses[i[1]] = losses.get(i[1], 0) + 1

        # above just made a set for winners and a map for # of losses each faced

        for i in losses:
            if losses[i] == 1:
                answer[1].append(i)

        for i in winner:
            if losses.get(i, 0) >= 1:
                continue
            else:
                answer[0].append(i)

        answer[0].sort()
        answer[1].sort()

        return answer


# (args_tuple, expected)
TESTS = [
    (([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]],),
     [[1, 2, 10], [4, 5, 7, 8]]),
    (([[2, 3], [1, 3], [5, 4], [6, 4]],), [[1, 2, 5, 6], []]),
    (([[1, 2]],), [[1], [2]]),
    (([[1, 2], [2, 1]],), [[], [1, 2]]),       # everyone lost exactly once
    (([[1, 2], [1, 3], [1, 4]],), [[1], [2, 3, 4]]),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.findWinners(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
