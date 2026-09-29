"""
Top K Frequent Elements  [Medium]
Arrays & Hashing

LeetCode: https://leetcode.com/problems/top-k-frequent-elements/
NeetCode: https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150

Pattern: bucket sort by count, index = frequency
Time:   O(n)    count, bucket, then walk the buckets
Space:  O(n)

The idea in one sentence:
Count every value, then drop each value into the bucket whose index IS its
count, and read the buckets from the high end until k values are collected.

Why bucket sort is allowed here: the key I am sorting by is a count, and a
count can never exceed len(nums). A bounded key means I can use it as an array
index instead of comparing, which is what turns O(n log n) sorting into O(n).

Where I got stuck:
Five separate mistakes, none of them the algorithm.
  1. `map.get(n, 0) + 1` with no assignment, so the map stayed empty and the
     whole thing returned []. Third time I have made this exact mistake: an
     expression changes nothing, only `=` writes back.
  2. `range(len(nums)-1)` in the counting loop, skipping the last element.
  3. `[[]] * (len(nums)+1)` creates n+1 references to ONE list, so appending to
     any bucket appends to all of them. The comprehension is required.
  4. Then overcorrected the bucket count to len(nums)-1, which is too few: if
     every element is identical the count equals len(nums), so I need a bucket
     at that index, hence len(nums)+1.
  5. A `break_all` flag checked inside the inner loop, after the `break`, where
     it could never run. Returning directly from inside the loop deleted the
     whole problem.

Verified against a reference on 20,000 random inputs, 0 mismatches.

One gap left: there is no fallback `return` after the loops, so if k were ever
larger than the number of distinct values this returns None. LeetCode
guarantees a valid k, so it passes, but it is a real hole.
"""
from typing import List, Optional


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}
        freq = [[] for _ in range(len(nums)+1)]

        # need a bucket at EVERY single one. if index = freq, then it must be
        # from 0 --> len(nums) + 1, since it starts at 0

        for n in nums:
            map[n] = map.get(n, 0) + 1

        for n, c in map.items():
            freq[c].append(n)

        answer = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer


# (args_tuple, expected_as_a_set — any order is accepted)
TESTS = [
    (([1, 1, 1, 2, 2, 3], 2), {1, 2}),
    (([1], 1), {1}),
    (([1, 2], 2), {1, 2}),
    (([4, 4, 4, 4], 1), {4}),          # one distinct value, count == len(nums)
    (([1, 1, 2, 2, 3, 3], 3), {1, 2, 3}),
    (([3, 0, 1, 0], 2), {0, 3}),
    (([5, 5, 4, 4, 3], 2), {5, 4}),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.topKFrequent(*args)
        ok = got is not None and set(got) == want
        print(f"{'PASS' if ok else 'FAIL'} #{i}  got={got!r} want(any order)={want!r}")
