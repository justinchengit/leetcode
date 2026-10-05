"""
Binary Tree Zigzag Level Order Traversal  [Medium]
LeetCode 103 — https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Study guide: Trees and Graphs > Binary trees - BFS
Not part of NeetCode 150.

Pattern: BFS level by level, with the level buffer filled from alternating ends
Time:   O(n)
Space:  O(w)   w = widest level

The idea in one sentence:
Do a normal level-order BFS, but on odd levels push each value onto the FRONT
of the level buffer instead of the back, so the row comes out reversed without
reversing anything.

The load-bearing line is `level_set = len(queue)`: snapshotting the queue size
before the inner loop is what keeps each round to exactly one level, since the
children being enqueued would otherwise extend the same loop.

Note: appendleft is one of two equally good options; collecting normally and
reversing the list on odd levels is also O(k) per level, so same total cost.
The traversal order never changes, only how the row is assembled.

Note: `deque` works on LeetCode without an import because their harness
pre-imports it. Running this file locally needs the import below.
"""
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = deque([root])
        result = []
        counter = 0

        while queue:
            level_set = len(queue)
            this_level = deque()

            for _ in range(level_set):

                value = queue.popleft()
                if counter % 2 == 0:
                    this_level.append(value.val)
                else:
                    this_level.appendleft(value.val)

                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)

            result.append(list(this_level))
            counter += 1

        return result


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
    ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
    ([1], [[1]]),
    ([], []),
    ([1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]]),
    ([1, 2, 3, 4, 5, 6, 7], [[1], [3, 2], [4, 5, 6, 7]]),
    ([1, None, 2, None, 3], [[1], [2], [3]]),   # skewed, one node per level
]

if __name__ == "__main__":
    s = Solution()
    for i, (vals, want) in enumerate(TESTS, 1):
        got = s.zigzagLevelOrder(build(vals))
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
