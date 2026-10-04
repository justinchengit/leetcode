"""
Simplify Path  [Medium]
LeetCode 71 — https://leetcode.com/problems/simplify-path/
Study guide: Stacks and Queues > String problems
Not part of NeetCode 150.

Pattern: split on the separator, then a stack of directory names
Time:   O(n)
Space:  O(n)

The idea in one sentence:
Splitting on "/" turns the path into tokens, and then the whole problem is a
stack: ".." pops, "" and "." are noise, anything else is a directory to push.

Optimal: one split and one pass, each token handled once.

Why splitting first makes it easy: it removes the duplicate-slash problem for
free, because consecutive slashes produce empty tokens that get skipped by the
same branch that skips ".". No separate cleanup pass is needed.

Note: the third branch (`".." and not stack`) is only needed because the first
branch requires a non-empty stack. Writing it as `if word == "..": if stack:
stack.pop()` folds both cases into one and the branch disappears.
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []

        new_string = path.split('/')

        for word in new_string:
            if word == ".." and stack:
                stack.pop()
            elif word == "" or word == ".":
                continue
            elif word == ".." and not stack:
                continue
            else:
                stack.append(word)

        return "/" + "/".join(stack)


# (args_tuple, expected)
TESTS = [
    (("/home/",), "/home"),
    (("/home//foo/",), "/home/foo"),            # duplicate slashes
    (("/home/user/Documents/../Pictures",), "/home/user/Pictures"),
    (("/../",), "/"),                           # .. at the root does nothing
    (("/.../",), "/..."),                       # three dots is a real name
    (("/a/./b/../../c/",), "/c"),
    (("/",), "/"),
    (("/a//b////c/d//././/..",), "/a/b/c"),
]

if __name__ == "__main__":
    s = Solution()
    for i, (args, want) in enumerate(TESTS, 1):
        got = s.simplifyPath(*args)
        print(f"{'PASS' if got == want else 'FAIL'} #{i}  got={got!r} want={want!r}")
