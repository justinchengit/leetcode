"""
Remove Duplicates from Sorted List  [Easy]
LeetCode 83 — https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Study guide: Linked Lists > Fast and slow pointers
Not part of NeetCode 150.

Pattern: one pointer, splice out the next node instead of advancing
Time:   O(n)
Space:  O(1)

The idea in one sentence:
The list is sorted, so duplicates are always adjacent; whenever the next node
matches the current one, unlink it and look again without moving.

The key insight, which I got right: do NOT advance after a deletion. The new
next node might be another duplicate, so the pointer has to stay put and
re-check. Advancing every iteration is the classic bug here and it fails on
runs of three or more, like [1,1,1].

Also correct: the `temp != None` half of the guard covers the empty list, and
`temp.next != None` is what makes `temp.next.val` safe to read.

Optimal: one pass, nothing allocated.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        temp = head

        while temp != None and temp.next != None:
            if temp.next.val == temp.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head


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
    ([1, 1, 2], [1, 2]),
    ([1, 1, 2, 3, 3], [1, 2, 3]),
    ([], []),                      # empty list
    ([1], [1]),
    ([1, 1, 1], [1]),              # run of three, breaks if you advance on delete
    ([1, 2, 3], [1, 2, 3]),        # nothing to remove
    ([1, 1, 1, 1, 2, 2, 3], [1, 2, 3]),
]

if __name__ == "__main__":
    s = Solution()
    for i, (values, want) in enumerate(TESTS, 1):
        got = to_list(s.deleteDuplicates(build(values)))
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  {values} -> got={got!r} want={want!r}")
