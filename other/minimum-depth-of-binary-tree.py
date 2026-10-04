"""
Minimum Depth of Binary Tree  [Easy]
LeetCode 111 — https://leetcode.com/problems/minimum-depth-of-binary-tree/
Study guide: Trees and Graphs > Binary trees - DFS
Not part of NeetCode 150.

Pattern: DFS recursion, with a special case for nodes that have one child
Time:   O(n)
Space:  O(h)   the call stack, h = height

The idea in one sentence:
The minimum depth is one plus the smaller of the two child depths, EXCEPT that
a missing child is not a path to a leaf and must not be counted as depth 0.

The crux, which I got right: min() would be wrong on its own. For a node with
only a right child, min(minDepth(None), minDepth(right)) is min(0, k) = 0, and
the node would report depth 1 as if it were a leaf. A missing child has to be
skipped, not minimised over. This is exactly why minDepth needs branches that
maxDepth does not.

Note: the explicit leaf check (`not root.right and not root.left: return 1`) is
dead code. If both children are missing, the `not root.left` branch below
returns minDepth(None) + 1 = 1 anyway. Harmless, but it is not load-bearing.

Better in practice: BFS. Level-order can stop the moment it meets its first
leaf, while this DFS explores every node even when a leaf sits one level down.
Same O(n) worst case, much faster on a tree with one shallow leaf and one deep
subtree.
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        if not root.right and not root.left:
            return 1

        if not root.left:
            return self.minDepth(root.right) + 1

        # If right child is missing, force it to check the left side
        if not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


def build(vals):
    """Level-order list with None for missing nodes."""
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
    ([3, 9, 20, None, None, 15, 7], 2),
    ([2, None, 3, None, 4, None, 5, None, 6], 5),   # skewed, the one-child case
    ([], 0),
    ([1], 1),
    ([1, 2], 2),
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, None, 3, None], 3),                     # left-skewed
]

if __name__ == "__main__":
    s = Solution()
    for i, (vals, want) in enumerate(TESTS, 1):
        got = s.minDepth(build(vals))
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  {vals} -> got={got!r} want={want!r}")
