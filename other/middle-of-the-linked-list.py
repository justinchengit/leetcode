"""
Middle of the Linked List  [Easy]
LeetCode 876 — https://leetcode.com/problems/middle-of-the-linked-list/
Study guide: Linked Lists > Fast and slow pointers
Not part of NeetCode 150.

Pattern: fast and slow pointers, fast moves two nodes per step
Time:   O(n)
Space:  O(1)

The idea in one sentence:
Move one pointer two nodes for every one node the other moves, so when the fast
one runs off the end the slow one is exactly halfway.

Why this is optimal: you cannot know the middle without reaching the end, so
O(n) time is the floor, and this does it in a single pass with no length count
and no extra storage.

Correction to my note: the loop guard is `fast != None AND fast.next != None`,
not "or". Both have to be true, because the step reads fast.next.next, which
needs fast and fast.next to both exist. With `or` it would crash.

On even-length lists this returns the SECOND middle node, which is what the
problem asks for, and it falls out of the loop for free rather than needing a
special case.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow


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


# (input_values, expected_list_from_the_middle_onward)
TESTS = [
    ([1, 2, 3, 4, 5], [3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], [4, 5, 6]),   # even length, second middle
    ([1], [1]),
    ([1, 2], [2]),
    ([1, 2, 3], [2, 3]),
]

if __name__ == "__main__":
    s = Solution()
    for i, (values, want) in enumerate(TESTS, 1):
        got = to_list(s.middleNode(build(values)))
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  {values} -> got={got!r} want={want!r}")
