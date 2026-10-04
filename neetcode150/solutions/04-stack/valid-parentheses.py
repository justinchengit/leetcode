"""
Valid Parentheses  [Easy]
Stack

LeetCode: https://leetcode.com/problems/valid-parentheses/
NeetCode: https://neetcode.io/problems/validate-parentheses?list=neetcode150
Study guide: Stacks and Queues > String problems

Pattern: stack, push openers and pop on a matching closer
Time:   O(n)
Space:  O(n)

The idea in one sentence:
Brackets close in the reverse order they opened, which is exactly a stack, so
push every opener and require each closer to match whatever is on top.

Optimal: every character is pushed and popped at most once.

Two things I learned, both right:
  - Check the stack is non-empty BEFORE reading stack[-1], otherwise a leading
    closer like ")" crashes instead of returning False.
  - A dict from closer to opener beats three separate comparisons, and it
    doubles as the "is this a closing brace" test via `if c in mapping`.

Note: `if not stack: return True else: return False` is just `return not stack`.
"""
from typing import List, Optional


class Solution:
    def isValid(self, s: str) -> bool:

        # first time using a stack for an actual usecase: will be empty if they cancel out
        # cancel condition if they are the same type

        mapping = {")": "(", "}": "{", "]": "["}

        stack = []

        for c in s:
            # closing brace: and make sure stack has stuff inside
            if c in mapping:
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False


# (args_tuple, expected)
TESTS = [
    (("()",), True),
    (("()[]{}",), True),
    (("(]",), False),
    (("([)]",), False),      # correctly nested count, wrong order
    (("{[]}",), True),
    (("",), True),
    ((")",), False),         # closer first, the empty-stack case
    (("(",), False),         # never closed
    (("((",), False),
    (("{[()]}",), True),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.isValid(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
