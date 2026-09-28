"""
Max Consecutive Ones III  [Medium]
LeetCode 1004 — https://leetcode.com/problems/max-consecutive-ones-iii/
Study guide: Arrays and Strings > Sliding window (variable size)
Not part of NeetCode 150.

Pattern: variable-size sliding window, at most k zeros allowed inside
Time:   O(n)    each step moves i or j, each bounded by n
Space:  O(1)

The idea in one sentence:
Keep the widest window that contains no more than k zeros, taking a 1 for free
and paying for a 0 out of the budget, and when the budget is gone move the left
edge up until a refund frees space.

Where I got stuck:
A lot, and almost none of it was the algorithm.
  1. Counted ones and returned `best + zero`, which glues a maximum from one
     moment onto a live count from a different moment. It returned 2 on [0,0]
     with k=1 where no valid window is longer than 1.
  2. The answer is a LENGTH, so what gets recorded is j - i + 1 (equivalently
     one + zero). Counting ones is not what the problem asks for.
  3. `zero < k` in the wrong place: with exactly k zeros spent, an incoming 1 is
     still free. Deciding on the budget instead of on what is entering lost
     [1,0,1] with k=1, where all three fit.
  4. Primed the window with j = 1 and read nums[1] before knowing it existed,
     which crashed on every single-element array.
  5. Wrote an extend branch with a bare `continue`, changing nothing, so it
     span forever.
  6. Forgot `j += 1` in both extend branches, same infinite loop again.

The four questions to ask, in this order, for any window problem:
  1. What is the answer measured in?   -> a length, so record j - i + 1
  2. What makes a window illegal?      -> more than k zeros, so count zeros only
  3. Which pointer drives the loop?    -> the right one, always forward
  4. What does the left one do?        -> repair only, and never rewind

Why j = -1 works: j is the last index INSIDE the window, so length is
j - i + 1, and an empty window needs j one step before the start. nums[j + 1]
then always means "the next candidate", so no priming block is needed and the
loop bound is checked before any read.

Verified against a brute force on 30,000 random arrays, 0 mismatches.

`one` is dead weight in the end, since one + zero is just the window length.
The shorter shape is: extend j every step, then `while zero > k` move i, then
record, which removes the branching entirely.

My note after solving (self-rated confidence 2.5): I understand the idea and I
understand the flow in and out of the window. What I cannot do yet is reach for
the efficient, correct structure on the first try. More exposure and more
thinking time will bring this down.

What that means concretely: the failures were never about what a sliding window
is, they were about bookkeeping. Where the pointers start, which one owns the
loop, what gets counted, when the answer gets recorded. So the drill is not
"learn sliding window" again, it is writing the invariant line down before
typing: the window is nums[i..j], j enters, i repairs, the answer is a length.
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # use sliding window, j = -1 means the window starts empty

        i = 0
        j = -1
        one = 0
        zero = 0
        best = 0

        while j < len(nums) - 1:
            if nums[j + 1] == 1:
                one += 1
                j += 1
                if one + zero > best:
                    best = one + zero
            elif zero < k:
                zero += 1
                j += 1
                if one + zero > best:
                    best = one + zero
            else:
                if nums[i] == 1:
                    one -= 1
                    i += 1
                else:
                    zero -= 1
                    i += 1

        return best


# (args_tuple, expected)
TESTS = [
    (([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6),
    (([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1], 3), 10),
    (([1, 1, 1, 1], 0), 4),      # no flips needed
    (([0, 0, 0], 0), 0),         # no flips allowed, no ones
    (([0, 0, 0], 2), 2),         # fewer ones than budget
    (([1, 0, 1], 1), 3),         # a 1 is free even with the budget spent
    (([1], 0), 1),               # single element, would crash the old priming
    (([0], 0), 0),
    (([0, 0], 1), 1),
    (([1, 0, 0, 1, 1, 1], 1), 4),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.longestOnes(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
