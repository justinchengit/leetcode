"""
Maximum Difference Between Node and Ancestor  [Medium]
LeetCode 1026 — https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
Study guide: Trees and Graphs > Binary trees - DFS
Not part of NeetCode 150.

Pattern: DFS carrying state DOWN the tree, answer resolved at the bottom
Time:   O(n)
Space:  O(h)

The idea in one sentence:
The biggest gap on any root-to-leaf path is just that path's max minus its min,
so carry the running max and min down each branch and take the difference when
the path ends.

Why this works at all: any ancestor-descendant pair lies on one root-to-leaf
path, and the largest difference on a path is always between its extremes. So
there is no need to compare every pair, only to track two numbers per path.

The direction is the thing to remember. Most tree DFS problems compute a value
coming back UP (minDepth, diameter). This one pushes state DOWN as arguments
and only reads the answer at the null node, where the path is complete. Both
shapes are DFS; which one you need depends on whether the answer depends on
where you came from or on what is below you.

Note: the diff gets computed at each of a leaf's two null children, so the same
value is produced twice. Harmless. Returning curr_max - curr_min at the leaf
itself avoids it.

Crashes on an empty tree, since `root.val` is read before the None check.
LeetCode guarantees at least 2 nodes, so it passes.
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def dfs(root, curr_max, curr_min):

            # feed root, root.val, root.val, where smallest = 0 since vals are the same

            if not root:
                return curr_max - curr_min

            curr_max = max(root.val, curr_max)
            curr_min = min(root.val, curr_min)

            left_diff = dfs(root.left, curr_max, curr_min)
            right_diff = dfs(root.right, curr_max, curr_min)

            return max(left_diff, right_diff)

        return dfs(root, root.val, root.val)


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
    ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], 7),
    ([1, None, 2, None, 0, None, 3], 3),
    ([1], 0),                       # one node, no ancestor pair
    ([1, 2], 1),
    ([5, 1, 9], 4),                 # the extremes are on different branches
    ([2, None, 1], 1),
]

if __name__ == "__main__":
    s = Solution()
    for i, (vals, want) in enumerate(TESTS, 1):
        got = s.maxAncestorDiff(build(vals))
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  {vals} -> got={got!r} want={want!r}")
