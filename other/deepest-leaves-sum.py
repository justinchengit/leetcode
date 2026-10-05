"""
Deepest Leaves Sum  [Medium]
LeetCode 1302 — https://leetcode.com/problems/deepest-leaves-sum/
Study guide: Trees and Graphs > Binary trees - BFS
Not part of NeetCode 150.

Pattern: level-order BFS, answer taken from the last level reached
Time:   O(n)
Space:  O(n) as written, O(w) if only the current level is kept

The idea in one sentence:
BFS finishes each level before starting the next, so whatever level the queue
empties on is the deepest one, and its sum is the answer.

The one optimization: `result` accumulates EVERY level but only the last one is
ever read, so the earlier lists are dead weight. Overwriting a single
`last_level = current_level` each round drops the space from O(n) to O(w),
where w is the widest level. Same time either way.

Note: crashes on an empty tree, since deque([None]) enters the loop and reads
value.val. LeetCode guarantees at least one node.

BFS is the right call here. DFS also works but needs you to track the maximum
depth seen and reset the running sum whenever a deeper level appears, which is
more state and more places to be wrong.
"""
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        queue = deque([root])
        result = []

        while queue:
            level_set = len(queue)
            current_level = []

            for _ in range(level_set):

                value = queue.popleft()
                current_level.append(value.val)

                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)

            result.append(current_level)

        return sum(result[-1])


def build(vals):
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = [root]
    i = 1
    while q and i < len(vals):
        node = q.pop(0)
        if i < len(vals):
            v = vals[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
        if i < len(vals):
            v = vals[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
    return root


# (level_order_values, expected)
TESTS = [
    ([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8], 15),
    ([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5], 19),
    ([1], 1),
    ([1, 2, 3], 5),                      # both leaves are deepest
    ([1, 2, None, 3, None], 3),          # skewed, one deepest leaf
    ([50, 2, 3], 5),                     # root is huge but not deepest
]

if __name__ == "__main__":
    s = Solution()
    for i, (vals, want) in enumerate(TESTS, 1):
        got = s.deepestLeavesSum(build(vals))
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  {vals} -> got={got!r} want={want!r}")
