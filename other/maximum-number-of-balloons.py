"""
Maximum Number of Balloons  [Easy]
LeetCode 1189 — https://leetcode.com/problems/maximum-number-of-balloons/
Study guide: Hashing > Counting
Not part of NeetCode 150.

Pattern: character counts, then the bottleneck letter decides the answer
Time:   O(n)
Space:  O(1)   at most 26 keys

The idea in one sentence:
"balloon" needs b, a, n once and l, o twice, so count the letters and the
answer is the smallest supply after halving the two doubled letters.

Already optimal at O(n). Three cleanups:
  - Counting l and o as 0.5 each works (0.5 is exact in binary, so no float
    drift), but counting whole letters and dividing with // at the end is the
    usual way: min(c['b'], c['a'], c['l']//2, c['o']//2, c['n']).
  - "bapn" has a stray p. "balloon" contains no p, and nothing ever reads
    map['p'], so it is harmless, but it is misleading. It should be "ban".
  - `else: continue` at the end of a loop body does nothing and can go.
"""


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        map = {}

        for i in text:
            if i in "bapn":
                map[i] = map.get(i, 0) + 1
            elif i in "ol":
                map[i] = map.get(i, 0) + 0.5
            else:
                continue

        return int(min(
            map.get('b', 0),
            map.get('a', 0),
            map.get('l', 0),
            map.get('o', 0),
            map.get('n', 0)
        ))


# (args_tuple, expected)
TESTS = [
    (("nlaebolko",), 1),
    (("loonbalxballpoon",), 2),
    (("leetcode",), 0),
    (("balloon",), 1),
    (("balloonballoon",), 2),
    (("bbaall",), 0),        # no o or n at all
    (("balloonn",), 1),      # extra n does not help
    (("balllloooon",), 2),   # 4 l and 4 o but only one b, a, n
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.maxNumberOfBalloons(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
