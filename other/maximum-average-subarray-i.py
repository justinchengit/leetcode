"""
Maximum Average Subarray I  [Easy]
LeetCode 643 — https://leetcode.com/problems/maximum-average-subarray-i/
Study guide: Arrays and Strings > Sliding window (fixed size)
Not part of NeetCode 150.

Pattern: fixed-size sliding window, prime the first window then slide it
Time:   O(n)
Space:  O(1)

The idea in one sentence:
Sum the first k elements once, then move the window one step at a time by
adding the entering element and subtracting the leaving one, keeping the best
total seen.

Where I got stuck:
Everything except the algorithm. The mistakes, in order:
  1. Conflated the running total with the answer, so when the `if` skipped an
     update `sum` stopped matching the window and produced averages no window
     could actually make.
  2. An expression alone changes nothing, only `=` writes back. `sum + x - y`
     as a condition computes and discards.
  3. Let `j` bound BOTH the priming loop and the slide, so fixing j for the
     slide silently made the priming loop sum k+1 elements and crash when
     k == len(nums).
  4. Started `i` at 1 when the first element to leave is index 0.
  5. Seeded `best = 0`, which never considers the first window and returns 0.0
     on an all-negative array.

My note after solving: I used a sliding window. I need to remember to use k
properly, because I keep reusing one variable for two different jobs. I want a
clear, fixed shape for these: define the window sum before the loop, then keep
a running total and a best, since the window moves by a fixed amount. Without a
fixed k the whole problem changes.

The invariant to write down before coding, every time:
  before each slide the window is [i .. j-1], j enters, i leaves

The lesson: in a FIXED-size window there is no decision about which pointer to
move. Both move every step, unconditionally. The only decision is whether to
record a new best. The "push left if it is worse" instinct belongs to the
variable-size window (1004), not here.
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # use floats
        # iterate from one end to the next

        i = 0
        j = k
        sum = 0
        z = 0

        while z <= j-1:
            sum = nums[z] + sum
            z += 1

        best = sum

        while j <= len(nums) - 1:
            if sum + nums[j] - nums[i] > best:
                best = sum + nums[j] - nums[i]
            sum = sum + nums[j] - nums[i]
            i += 1
            j += 1

        avg = float(best/k)

        return avg


# (args_tuple, expected)
TESTS = [
    (([1, 12, -5, -6, 50, 3], 4), 12.75),
    (([5], 1), 5.0),
    (([-5], 1), -5.0),
    (([0, 1, 1, 3, 3], 4), 2.0),
    (([-1, -2, -3, -4], 2), -1.5),   # all negative, best is the least bad
    (([4, 2, 1, 3, 3], 2), 3.0),     # best window is NOT the first one
    (([9, 1, 1, 1], 2), 5.0),        # best window IS the first one
    (([1, 2, 3], 3), 2.0),           # k == len(nums), no slide happens
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.findMaxAverage(*args)
        ok = abs(got - want) < 1e-9
        print(f"{'PASS' if ok else 'FAIL'} #{i}  got={got!r} want={want!r}")
