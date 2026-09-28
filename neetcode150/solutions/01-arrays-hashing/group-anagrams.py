"""
Group Anagrams  [Medium]
Arrays & Hashing

LeetCode: https://leetcode.com/problems/group-anagrams/
NeetCode: https://neetcode.io/problems/anagram-groups?list=neetcode150

Pattern: hash map keyed by a canonical form of each word (its sorted letters)
Time:   O(n * k log k)   n words of length up to k
Space:  O(n * k)

The idea in one sentence (write this AFTER you solve it — this is the part
you'll actually reread before an interview):
Anagrams collapse to the same string once sorted, so use that sorted string as
a dictionary key and every word lands in the right bucket in one pass.

Where I got stuck:
Initialising the map. I did it with `if key in d / else d[key] = [word]`, which
works; the idiom for exactly this is `collections.defaultdict(list)`, or
`d.setdefault(key, []).append(word)`. Also learned `list(d.values())` hands
back the buckets as a list of lists.

Note: sorted(word) works on the string directly, no need to build `arr` first.

Possible upgrade: a 26-length tuple of letter counts as the key instead of the
sorted string drops the k log k to k.
"""
from typing import List, Optional


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array of strs, group them into sublists
        d = {}

        for word in strs:
            arr = []
            for c in word:
                arr.append(c)
            key = "".join(sorted(arr))
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]

        return list(d.values())


# (args_tuple, expected)
# dicts keep insertion order, so group order is first-appearance order
TESTS = [
    ((["eat", "tea", "tan", "ate", "nat", "bat"],),
     [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
    (([""],), [[""]]),
    ((["a"],), [["a"]]),
    ((["abc", "cba", "bca", "xyz"],), [["abc", "cba", "bca"], ["xyz"]]),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.groupAnagrams(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
    if not TESTS:
        print("No tests yet — add a couple of cases to TESTS.")
