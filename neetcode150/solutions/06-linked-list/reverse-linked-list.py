"""
Reverse Linked List  [Easy]
Linked List

LeetCode: https://leetcode.com/problems/reverse-linked-list/
NeetCode: https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150
Study guide: Linked Lists > Reversing a linked list

Pattern: three pointers, flip each next pointer backward as you walk
Time:   O(n)
Space:  O(1)

The idea in one sentence:
Walk the list once, and at each node stash the next node, point the current
node back at the previous one, then shift both prev and curr forward.

Solved this one without reading a solution.

The ordering is the whole problem: `temp = curr.next` has to happen BEFORE
`curr.next = prev`, or the rest of the list is stranded with no way back to it.

Return `prev`, not `head`: when the loop ends curr is None and prev is sitting
on the last node visited, which is the new head. `head` is now the tail.

Note: the `if head == None or head.next == None: return head` guard is dead
code. The loop already handles both. Empty list means curr is None, the body
never runs, and prev (None) is returned. Single node means one pass that
returns that node. Same kind of unnecessary guard as the one on the pangram and
substring problems.
"""
from typing import List, Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head == None or head.next == None:
            return head

        curr = head
        prev = None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


# (input_values, expected)
TESTS = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([], []),
    ([1, 1, 2], [2, 1, 1]),
]

if __name__ == "__main__":
    s = Solution()
    for i, (values, want) in enumerate(TESTS, 1):
        got = to_list(s.reverseList(build(values)))
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  {values} -> got={got!r} want={want!r}")
