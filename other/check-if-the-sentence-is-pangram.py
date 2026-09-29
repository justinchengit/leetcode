"""
Check if the Sentence Is Pangram  [Easy]
LeetCode 1832 — https://leetcode.com/problems/check-if-the-sentence-is-pangram/
Study guide: Hashing > Checking for existence
Not part of NeetCode 150.

Pattern: set for distinct membership, then count the distinct letters
Time:   O(n)
Space:  O(1)   at most 26 entries, bounded by the alphabet not the input

The idea in one sentence:
A pangram is exactly a sentence whose distinct letters number 26, so collect
them in a set and check its size.

Notes for next time:
  - The `if char != " "` guard is not needed: this problem's input is lowercase
    letters only. Harmless, but it would also be insufficient if punctuation
    were allowed, so it buys nothing either way.
  - `if cond: return True / return False` collapses to `return cond`, same
    thing I noted on valid-anagram.
  - Could exit early the moment the set hits 26 instead of reading the rest of
    the sentence. Same O(n) worst case, faster in practice.
  - A sentence shorter than 26 characters can never be a pangram, so that is a
    one-line early bail too.
"""


class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        alphabet = set()

        for char in sentence:
            if char != " ":
                alphabet.add(char)

        if len(alphabet) == 26:
            return True

        return False


# (args_tuple, expected)
TESTS = [
    (("thequickbrownfoxjumpsoverthelazydog",), True),
    (("leetcode",), False),
    (("abcdefghijklmnopqrstuvwxyz",), True),
    (("abcdefghijklmnopqrstuvwxy",), False),   # 25 letters, one short
    (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",), False),
    (("",), False),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.checkIfPangram(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
