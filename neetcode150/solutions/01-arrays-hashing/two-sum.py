"""
Two Sum  [Easy]
Arrays & Hashing

LeetCode: https://leetcode.com/problems/two-sum/
NeetCode: https://neetcode.io/problems/two-integer-sum?list=neetcode150

Pattern: one pass, dict of value -> index, look up the complement before inserting
Time:   O(n)
Space:  O(n)

The idea in one sentence (write this AFTER you solve it — this is the part
you'll actually reread before an interview):
I never search for the partner because I can compute it (target - num), so I
keep a map of every value I have passed and ask whether the partner is already
in it.

Where I got stuck:
The ordering. The `if` has to come BEFORE `d[a] = i`: on [5, 5] with target 10,
writing first means the second 5 overwrites index 0 with index 1, and then the
pair is gone. Checking first means the old index is still sitting there when I
need it, so the overwrite afterwards is harmless.

First pass was the O(n^2) double loop (kept below as FirstPass). Two leftovers
in this version that are dead once the ordering is right: `d[goal] != i` can
never be false, since d only holds indices before i, and sorted() is redundant
because d[goal] is always the earlier index.
"""
from typing import List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices i and j of the nums array that adds to a target
        # iterate i, put in dict. then search to see if it's in there...

        d = {}

        for i, a in enumerate(nums):

            goal = target - a
            if goal in d and d[goal] != i:
                arr = [i, d[goal]]
                success = sorted(arr)
                return success
            d[a] = i


class FirstPass:
    """O(n^2) brute force over every pair, my first attempt."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i == j:
                    continue
                if a + b == target:
                    return sorted([i, j])


# (args_tuple, expected)
TESTS = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
    (([5, 5], 10), [0, 1]),          # the overwrite case
    (([-1, -2, -3, -4], -7), [2, 3]),
    (([0, 4, 3, 0], 0), [0, 3]),
]

if __name__ == "__main__":
    s = Solution()
    old = FirstPass()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.twoSum(*args)
        also = old.twoSum(*args)
        flag = "PASS" if got == want and also == want else "FAIL"
        print(f"{flag} #{i}  got={got!r} brute={also!r} want={want!r}")
    if not TESTS:
        print("No tests yet — add a couple of cases to TESTS.")
