# NeetCode 150

**0 / 150 solved**

`░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░` 0%

| Difficulty | Progress |
|---|---|
| Easy | `░░░░░░░░░░░░░░░░░░` 0/28 |
| Medium | `░░░░░░░░░░░░░░░░░░` 0/101 |
| Hard | `░░░░░░░░░░░░░░░░░░` 0/21 |

<details>
<summary><b>How I use this</b></summary>

```bash
python tools/nc.py next            # next unsolved problem + creates the stub file
python tools/nc.py next -c trees   # next one in a category
python tools/nc.py log two-sum -c 3 -m 25      # after solving: confidence 1-5, minutes
python tools/nc.py log two-sum -c 1 --hint     # --hint = I looked at the answer
python tools/nc.py review          # what's due for a second pass today
python tools/nc.py stats           # where I'm weak
python tools/nc.py csv             # export for the spreadsheet
```

**Confidence** is the whole point of the tracker: `1` no idea, `3` got there with
effort, `5` instant. It sets when the problem comes back — a 1 returns tomorrow, a
5 in five weeks. Rate honestly; rating yourself generous just means you meet the
problem again for the first time in the interview.

Rules I'm holding myself to: 30 minutes stuck, then read the solution, mark
`--hint`, and re-solve it from blank in a day or two. Never copy-paste a solution
in. Fill in the one-sentence summary at the top of each file after solving —
that's the part worth rereading later.

</details>

## Progress by category

| Category | Solved | |
|---|---|---|
| Arrays & Hashing | 0/9 | `░░░░░░░░░░░░░░` |
| Two Pointers | 0/5 | `░░░░░░░░░░░░░░` |
| Sliding Window | 0/6 | `░░░░░░░░░░░░░░` |
| Stack | 0/6 | `░░░░░░░░░░░░░░` |
| Binary Search | 0/7 | `░░░░░░░░░░░░░░` |
| Linked List | 0/11 | `░░░░░░░░░░░░░░` |
| Trees | 0/15 | `░░░░░░░░░░░░░░` |
| Heap / Priority Queue | 0/7 | `░░░░░░░░░░░░░░` |
| Backtracking | 0/10 | `░░░░░░░░░░░░░░` |
| Tries | 0/3 | `░░░░░░░░░░░░░░` |
| Graphs | 0/13 | `░░░░░░░░░░░░░░` |
| Advanced Graphs | 0/6 | `░░░░░░░░░░░░░░` |
| 1-D Dynamic Programming | 0/12 | `░░░░░░░░░░░░░░` |
| 2-D Dynamic Programming | 0/11 | `░░░░░░░░░░░░░░` |
| Greedy | 0/8 | `░░░░░░░░░░░░░░` |
| Intervals | 0/6 | `░░░░░░░░░░░░░░` |
| Math & Geometry | 0/8 | `░░░░░░░░░░░░░░` |
| Bit Manipulation | 0/7 | `░░░░░░░░░░░░░░` |

## Problems

<details>
<summary><b>Arrays & Hashing</b> &nbsp; 0/9</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 1 | Contains Duplicate | Easy |  |  |  | [LC](https://leetcode.com/problems/contains-duplicate/) · [NC](https://neetcode.io/problems/duplicate-integer?list=neetcode150) |
| [ ] | 2 | Valid Anagram | Easy |  |  |  | [LC](https://leetcode.com/problems/valid-anagram/) · [NC](https://neetcode.io/problems/is-anagram?list=neetcode150) |
| [ ] | 3 | Two Sum | Easy |  |  |  | [LC](https://leetcode.com/problems/two-sum/) · [NC](https://neetcode.io/problems/two-integer-sum?list=neetcode150) |
| [ ] | 4 | Group Anagrams | Medium |  |  |  | [LC](https://leetcode.com/problems/group-anagrams/) · [NC](https://neetcode.io/problems/anagram-groups?list=neetcode150) |
| [ ] | 5 | Top K Frequent Elements | Medium |  |  |  | [LC](https://leetcode.com/problems/top-k-frequent-elements/) · [NC](https://neetcode.io/problems/top-k-elements-in-list?list=neetcode150) |
| [ ] | 6 | Encode and Decode Strings | Medium |  |  |  | [LC](https://leetcode.com/problems/encode-and-decode-strings/) · [NC](https://neetcode.io/problems/string-encode-and-decode?list=neetcode150) |
| [ ] | 7 | Product of Array Except Self | Medium |  |  |  | [LC](https://leetcode.com/problems/product-of-array-except-self/) · [NC](https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150) |
| [ ] | 8 | Valid Sudoku | Medium |  |  |  | [LC](https://leetcode.com/problems/valid-sudoku/) · [NC](https://neetcode.io/problems/valid-sudoku?list=neetcode150) |
| [ ] | 9 | Longest Consecutive Sequence | Medium |  |  |  | [LC](https://leetcode.com/problems/longest-consecutive-sequence/) · [NC](https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150) |

</details>

<details>
<summary><b>Two Pointers</b> &nbsp; 0/5</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 10 | Valid Palindrome | Easy |  |  |  | [LC](https://leetcode.com/problems/valid-palindrome/) · [NC](https://neetcode.io/problems/is-palindrome?list=neetcode150) |
| [ ] | 11 | Two Sum II Input Array Is Sorted | Medium |  |  |  | [LC](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · [NC](https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150) |
| [ ] | 12 | 3Sum | Medium |  |  |  | [LC](https://leetcode.com/problems/3sum/) · [NC](https://neetcode.io/problems/three-integer-sum?list=neetcode150) |
| [ ] | 13 | Container With Most Water | Medium |  |  |  | [LC](https://leetcode.com/problems/container-with-most-water/) · [NC](https://neetcode.io/problems/max-water-container?list=neetcode150) |
| [ ] | 14 | Trapping Rain Water | Hard |  |  |  | [LC](https://leetcode.com/problems/trapping-rain-water/) · [NC](https://neetcode.io/problems/trapping-rain-water?list=neetcode150) |

</details>

<details>
<summary><b>Sliding Window</b> &nbsp; 0/6</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 15 | Best Time to Buy And Sell Stock | Easy |  |  |  | [LC](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · [NC](https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150) |
| [ ] | 16 | Longest Substring Without Repeating Characters | Medium |  |  |  | [LC](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · [NC](https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150) |
| [ ] | 17 | Longest Repeating Character Replacement | Medium |  |  |  | [LC](https://leetcode.com/problems/longest-repeating-character-replacement/) · [NC](https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=neetcode150) |
| [ ] | 18 | Permutation In String | Medium |  |  |  | [LC](https://leetcode.com/problems/permutation-in-string/) · [NC](https://neetcode.io/problems/permutation-string?list=neetcode150) |
| [ ] | 19 | Minimum Window Substring | Hard |  |  |  | [LC](https://leetcode.com/problems/minimum-window-substring/) · [NC](https://neetcode.io/problems/minimum-window-with-characters?list=neetcode150) |
| [ ] | 20 | Sliding Window Maximum | Hard |  |  |  | [LC](https://leetcode.com/problems/sliding-window-maximum/) · [NC](https://neetcode.io/problems/sliding-window-maximum?list=neetcode150) |

</details>

<details>
<summary><b>Stack</b> &nbsp; 0/6</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 21 | Valid Parentheses | Easy |  |  |  | [LC](https://leetcode.com/problems/valid-parentheses/) · [NC](https://neetcode.io/problems/validate-parentheses?list=neetcode150) |
| [ ] | 22 | Min Stack | Medium |  |  |  | [LC](https://leetcode.com/problems/min-stack/) · [NC](https://neetcode.io/problems/minimum-stack?list=neetcode150) |
| [ ] | 23 | Evaluate Reverse Polish Notation | Medium |  |  |  | [LC](https://leetcode.com/problems/evaluate-reverse-polish-notation/) · [NC](https://neetcode.io/problems/evaluate-reverse-polish-notation?list=neetcode150) |
| [ ] | 24 | Daily Temperatures | Medium |  |  |  | [LC](https://leetcode.com/problems/daily-temperatures/) · [NC](https://neetcode.io/problems/daily-temperatures?list=neetcode150) |
| [ ] | 25 | Car Fleet | Medium |  |  |  | [LC](https://leetcode.com/problems/car-fleet/) · [NC](https://neetcode.io/problems/car-fleet?list=neetcode150) |
| [ ] | 26 | Largest Rectangle In Histogram | Hard |  |  |  | [LC](https://leetcode.com/problems/largest-rectangle-in-histogram/) · [NC](https://neetcode.io/problems/largest-rectangle-in-histogram?list=neetcode150) |

</details>

<details>
<summary><b>Binary Search</b> &nbsp; 0/7</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 27 | Binary Search | Easy |  |  |  | [LC](https://leetcode.com/problems/binary-search/) · [NC](https://neetcode.io/problems/binary-search?list=neetcode150) |
| [ ] | 28 | Search a 2D Matrix | Medium |  |  |  | [LC](https://leetcode.com/problems/search-a-2d-matrix/) · [NC](https://neetcode.io/problems/search-2d-matrix?list=neetcode150) |
| [ ] | 29 | Koko Eating Bananas | Medium |  |  |  | [LC](https://leetcode.com/problems/koko-eating-bananas/) · [NC](https://neetcode.io/problems/eating-bananas?list=neetcode150) |
| [ ] | 30 | Find Minimum In Rotated Sorted Array | Medium |  |  |  | [LC](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) · [NC](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array?list=neetcode150) |
| [ ] | 31 | Search In Rotated Sorted Array | Medium |  |  |  | [LC](https://leetcode.com/problems/search-in-rotated-sorted-array/) · [NC](https://neetcode.io/problems/find-target-in-rotated-sorted-array?list=neetcode150) |
| [ ] | 32 | Time Based Key Value Store | Medium |  |  |  | [LC](https://leetcode.com/problems/time-based-key-value-store/) · [NC](https://neetcode.io/problems/time-based-key-value-store?list=neetcode150) |
| [ ] | 33 | Median of Two Sorted Arrays | Hard |  |  |  | [LC](https://leetcode.com/problems/median-of-two-sorted-arrays/) · [NC](https://neetcode.io/problems/median-of-two-sorted-arrays?list=neetcode150) |

</details>

<details>
<summary><b>Linked List</b> &nbsp; 0/11</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 34 | Reverse Linked List | Easy |  |  |  | [LC](https://leetcode.com/problems/reverse-linked-list/) · [NC](https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150) |
| [ ] | 35 | Merge Two Sorted Lists | Easy |  |  |  | [LC](https://leetcode.com/problems/merge-two-sorted-lists/) · [NC](https://neetcode.io/problems/merge-two-sorted-linked-lists?list=neetcode150) |
| [ ] | 36 | Linked List Cycle | Easy |  |  |  | [LC](https://leetcode.com/problems/linked-list-cycle/) · [NC](https://neetcode.io/problems/linked-list-cycle-detection?list=neetcode150) |
| [ ] | 37 | Reorder List | Medium |  |  |  | [LC](https://leetcode.com/problems/reorder-list/) · [NC](https://neetcode.io/problems/reorder-linked-list?list=neetcode150) |
| [ ] | 38 | Remove Nth Node From End of List | Medium |  |  |  | [LC](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) · [NC](https://neetcode.io/problems/remove-node-from-end-of-linked-list?list=neetcode150) |
| [ ] | 39 | Copy List With Random Pointer | Medium |  |  |  | [LC](https://leetcode.com/problems/copy-list-with-random-pointer/) · [NC](https://neetcode.io/problems/copy-linked-list-with-random-pointer?list=neetcode150) |
| [ ] | 40 | Add Two Numbers | Medium |  |  |  | [LC](https://leetcode.com/problems/add-two-numbers/) · [NC](https://neetcode.io/problems/add-two-numbers?list=neetcode150) |
| [ ] | 41 | Find The Duplicate Number | Medium |  |  |  | [LC](https://leetcode.com/problems/find-the-duplicate-number/) · [NC](https://neetcode.io/problems/find-duplicate-integer?list=neetcode150) |
| [ ] | 42 | LRU Cache | Medium |  |  |  | [LC](https://leetcode.com/problems/lru-cache/) · [NC](https://neetcode.io/problems/lru-cache?list=neetcode150) |
| [ ] | 43 | Merge K Sorted Lists | Hard |  |  |  | [LC](https://leetcode.com/problems/merge-k-sorted-lists/) · [NC](https://neetcode.io/problems/merge-k-sorted-linked-lists?list=neetcode150) |
| [ ] | 44 | Reverse Nodes In K Group | Hard |  |  |  | [LC](https://leetcode.com/problems/reverse-nodes-in-k-group/) · [NC](https://neetcode.io/problems/reverse-nodes-in-k-group?list=neetcode150) |

</details>

<details>
<summary><b>Trees</b> &nbsp; 0/15</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 45 | Invert Binary Tree | Easy |  |  |  | [LC](https://leetcode.com/problems/invert-binary-tree/) · [NC](https://neetcode.io/problems/invert-a-binary-tree?list=neetcode150) |
| [ ] | 46 | Maximum Depth of Binary Tree | Easy |  |  |  | [LC](https://leetcode.com/problems/maximum-depth-of-binary-tree/) · [NC](https://neetcode.io/problems/depth-of-binary-tree?list=neetcode150) |
| [ ] | 47 | Diameter of Binary Tree | Easy |  |  |  | [LC](https://leetcode.com/problems/diameter-of-binary-tree/) · [NC](https://neetcode.io/problems/binary-tree-diameter?list=neetcode150) |
| [ ] | 48 | Balanced Binary Tree | Easy |  |  |  | [LC](https://leetcode.com/problems/balanced-binary-tree/) · [NC](https://neetcode.io/problems/balanced-binary-tree?list=neetcode150) |
| [ ] | 49 | Same Tree | Easy |  |  |  | [LC](https://leetcode.com/problems/same-tree/) · [NC](https://neetcode.io/problems/same-binary-tree?list=neetcode150) |
| [ ] | 50 | Subtree of Another Tree | Easy |  |  |  | [LC](https://leetcode.com/problems/subtree-of-another-tree/) · [NC](https://neetcode.io/problems/subtree-of-a-binary-tree?list=neetcode150) |
| [ ] | 51 | Lowest Common Ancestor of a Binary Search Tree | Medium |  |  |  | [LC](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) · [NC](https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree?list=neetcode150) |
| [ ] | 52 | Binary Tree Level Order Traversal | Medium |  |  |  | [LC](https://leetcode.com/problems/binary-tree-level-order-traversal/) · [NC](https://neetcode.io/problems/level-order-traversal-of-binary-tree?list=neetcode150) |
| [ ] | 53 | Binary Tree Right Side View | Medium |  |  |  | [LC](https://leetcode.com/problems/binary-tree-right-side-view/) · [NC](https://neetcode.io/problems/binary-tree-right-side-view?list=neetcode150) |
| [ ] | 54 | Count Good Nodes In Binary Tree | Medium |  |  |  | [LC](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) · [NC](https://neetcode.io/problems/count-good-nodes-in-binary-tree?list=neetcode150) |
| [ ] | 55 | Validate Binary Search Tree | Medium |  |  |  | [LC](https://leetcode.com/problems/validate-binary-search-tree/) · [NC](https://neetcode.io/problems/valid-binary-search-tree?list=neetcode150) |
| [ ] | 56 | Kth Smallest Element In a Bst | Medium |  |  |  | [LC](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) · [NC](https://neetcode.io/problems/kth-smallest-integer-in-bst?list=neetcode150) |
| [ ] | 57 | Construct Binary Tree From Preorder And Inorder Traversal | Medium |  |  |  | [LC](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) · [NC](https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal?list=neetcode150) |
| [ ] | 58 | Binary Tree Maximum Path Sum | Hard |  |  |  | [LC](https://leetcode.com/problems/binary-tree-maximum-path-sum/) · [NC](https://neetcode.io/problems/binary-tree-maximum-path-sum?list=neetcode150) |
| [ ] | 59 | Serialize And Deserialize Binary Tree | Hard |  |  |  | [LC](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) · [NC](https://neetcode.io/problems/serialize-and-deserialize-binary-tree?list=neetcode150) |

</details>

<details>
<summary><b>Heap / Priority Queue</b> &nbsp; 0/7</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 60 | Kth Largest Element In a Stream | Easy |  |  |  | [LC](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · [NC](https://neetcode.io/problems/kth-largest-integer-in-a-stream?list=neetcode150) |
| [ ] | 61 | Last Stone Weight | Easy |  |  |  | [LC](https://leetcode.com/problems/last-stone-weight/) · [NC](https://neetcode.io/problems/last-stone-weight?list=neetcode150) |
| [ ] | 62 | K Closest Points to Origin | Medium |  |  |  | [LC](https://leetcode.com/problems/k-closest-points-to-origin/) · [NC](https://neetcode.io/problems/k-closest-points-to-origin?list=neetcode150) |
| [ ] | 63 | Kth Largest Element In An Array | Medium |  |  |  | [LC](https://leetcode.com/problems/kth-largest-element-in-an-array/) · [NC](https://neetcode.io/problems/kth-largest-element-in-an-array?list=neetcode150) |
| [ ] | 64 | Task Scheduler | Medium |  |  |  | [LC](https://leetcode.com/problems/task-scheduler/) · [NC](https://neetcode.io/problems/task-scheduling?list=neetcode150) |
| [ ] | 65 | Design Twitter | Medium |  |  |  | [LC](https://leetcode.com/problems/design-twitter/) · [NC](https://neetcode.io/problems/design-twitter-feed?list=neetcode150) |
| [ ] | 66 | Find Median From Data Stream | Hard |  |  |  | [LC](https://leetcode.com/problems/find-median-from-data-stream/) · [NC](https://neetcode.io/problems/find-median-in-a-data-stream?list=neetcode150) |

</details>

<details>
<summary><b>Backtracking</b> &nbsp; 0/10</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 67 | Subsets | Medium |  |  |  | [LC](https://leetcode.com/problems/subsets/) · [NC](https://neetcode.io/problems/subsets?list=neetcode150) |
| [ ] | 68 | Combination Sum | Medium |  |  |  | [LC](https://leetcode.com/problems/combination-sum/) · [NC](https://neetcode.io/problems/combination-target-sum?list=neetcode150) |
| [ ] | 69 | Combination Sum II | Medium |  |  |  | [LC](https://leetcode.com/problems/combination-sum-ii/) · [NC](https://neetcode.io/problems/combination-target-sum-ii?list=neetcode150) |
| [ ] | 70 | Permutations | Medium |  |  |  | [LC](https://leetcode.com/problems/permutations/) · [NC](https://neetcode.io/problems/permutations?list=neetcode150) |
| [ ] | 71 | Subsets II | Medium |  |  |  | [LC](https://leetcode.com/problems/subsets-ii/) · [NC](https://neetcode.io/problems/subsets-ii?list=neetcode150) |
| [ ] | 72 | Generate Parentheses | Medium |  |  |  | [LC](https://leetcode.com/problems/generate-parentheses/) · [NC](https://neetcode.io/problems/generate-parentheses?list=neetcode150) |
| [ ] | 73 | Word Search | Medium |  |  |  | [LC](https://leetcode.com/problems/word-search/) · [NC](https://neetcode.io/problems/search-for-word?list=neetcode150) |
| [ ] | 74 | Palindrome Partitioning | Medium |  |  |  | [LC](https://leetcode.com/problems/palindrome-partitioning/) · [NC](https://neetcode.io/problems/palindrome-partitioning?list=neetcode150) |
| [ ] | 75 | Letter Combinations of a Phone Number | Medium |  |  |  | [LC](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) · [NC](https://neetcode.io/problems/combinations-of-a-phone-number?list=neetcode150) |
| [ ] | 76 | N Queens | Hard |  |  |  | [LC](https://leetcode.com/problems/n-queens/) · [NC](https://neetcode.io/problems/n-queens?list=neetcode150) |

</details>

<details>
<summary><b>Tries</b> &nbsp; 0/3</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 77 | Implement Trie Prefix Tree | Medium |  |  |  | [LC](https://leetcode.com/problems/implement-trie-prefix-tree/) · [NC](https://neetcode.io/problems/implement-prefix-tree?list=neetcode150) |
| [ ] | 78 | Design Add And Search Words Data Structure | Medium |  |  |  | [LC](https://leetcode.com/problems/design-add-and-search-words-data-structure/) · [NC](https://neetcode.io/problems/design-word-search-data-structure?list=neetcode150) |
| [ ] | 79 | Word Search II | Hard |  |  |  | [LC](https://leetcode.com/problems/word-search-ii/) · [NC](https://neetcode.io/problems/search-for-word-ii?list=neetcode150) |

</details>

<details>
<summary><b>Graphs</b> &nbsp; 0/13</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 80 | Number of Islands | Medium |  |  |  | [LC](https://leetcode.com/problems/number-of-islands/) · [NC](https://neetcode.io/problems/count-number-of-islands?list=neetcode150) |
| [ ] | 81 | Max Area of Island | Medium |  |  |  | [LC](https://leetcode.com/problems/max-area-of-island/) · [NC](https://neetcode.io/problems/max-area-of-island?list=neetcode150) |
| [ ] | 82 | Clone Graph | Medium |  |  |  | [LC](https://leetcode.com/problems/clone-graph/) · [NC](https://neetcode.io/problems/clone-graph?list=neetcode150) |
| [ ] | 83 | Walls And Gates | Medium |  |  |  | [LC](https://leetcode.com/problems/walls-and-gates/) · [NC](https://neetcode.io/problems/islands-and-treasure?list=neetcode150) |
| [ ] | 84 | Rotting Oranges | Medium |  |  |  | [LC](https://leetcode.com/problems/rotting-oranges/) · [NC](https://neetcode.io/problems/rotting-fruit?list=neetcode150) |
| [ ] | 85 | Pacific Atlantic Water Flow | Medium |  |  |  | [LC](https://leetcode.com/problems/pacific-atlantic-water-flow/) · [NC](https://neetcode.io/problems/pacific-atlantic-water-flow?list=neetcode150) |
| [ ] | 86 | Surrounded Regions | Medium |  |  |  | [LC](https://leetcode.com/problems/surrounded-regions/) · [NC](https://neetcode.io/problems/surrounded-regions?list=neetcode150) |
| [ ] | 87 | Course Schedule | Medium |  |  |  | [LC](https://leetcode.com/problems/course-schedule/) · [NC](https://neetcode.io/problems/course-schedule?list=neetcode150) |
| [ ] | 88 | Course Schedule II | Medium |  |  |  | [LC](https://leetcode.com/problems/course-schedule-ii/) · [NC](https://neetcode.io/problems/course-schedule-ii?list=neetcode150) |
| [ ] | 89 | Graph Valid Tree | Medium |  |  |  | [LC](https://leetcode.com/problems/graph-valid-tree/) · [NC](https://neetcode.io/problems/valid-tree?list=neetcode150) |
| [ ] | 90 | Number of Connected Components In An Undirected Graph | Medium |  |  |  | [LC](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) · [NC](https://neetcode.io/problems/count-connected-components?list=neetcode150) |
| [ ] | 91 | Redundant Connection | Medium |  |  |  | [LC](https://leetcode.com/problems/redundant-connection/) · [NC](https://neetcode.io/problems/redundant-connection?list=neetcode150) |
| [ ] | 92 | Word Ladder | Hard |  |  |  | [LC](https://leetcode.com/problems/word-ladder/) · [NC](https://neetcode.io/problems/word-ladder?list=neetcode150) |

</details>

<details>
<summary><b>Advanced Graphs</b> &nbsp; 0/6</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 93 | Network Delay Time | Medium |  |  |  | [LC](https://leetcode.com/problems/network-delay-time/) · [NC](https://neetcode.io/problems/network-delay-time?list=neetcode150) |
| [ ] | 94 | Reconstruct Itinerary | Hard |  |  |  | [LC](https://leetcode.com/problems/reconstruct-itinerary/) · [NC](https://neetcode.io/problems/reconstruct-flight-path?list=neetcode150) |
| [ ] | 95 | Min Cost to Connect All Points | Medium |  |  |  | [LC](https://leetcode.com/problems/min-cost-to-connect-all-points/) · [NC](https://neetcode.io/problems/min-cost-to-connect-points?list=neetcode150) |
| [ ] | 96 | Swim In Rising Water | Hard |  |  |  | [LC](https://leetcode.com/problems/swim-in-rising-water/) · [NC](https://neetcode.io/problems/swim-in-rising-water?list=neetcode150) |
| [ ] | 97 | Alien Dictionary | Hard |  |  |  | [LC](https://leetcode.com/problems/alien-dictionary/) · [NC](https://neetcode.io/problems/foreign-dictionary?list=neetcode150) |
| [ ] | 98 | Cheapest Flights Within K Stops | Medium |  |  |  | [LC](https://leetcode.com/problems/cheapest-flights-within-k-stops/) · [NC](https://neetcode.io/problems/cheapest-flight-path?list=neetcode150) |

</details>

<details>
<summary><b>1-D Dynamic Programming</b> &nbsp; 0/12</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 99 | Climbing Stairs | Easy |  |  |  | [LC](https://leetcode.com/problems/climbing-stairs/) · [NC](https://neetcode.io/problems/climbing-stairs?list=neetcode150) |
| [ ] | 100 | Min Cost Climbing Stairs | Easy |  |  |  | [LC](https://leetcode.com/problems/min-cost-climbing-stairs/) · [NC](https://neetcode.io/problems/min-cost-climbing-stairs?list=neetcode150) |
| [ ] | 101 | House Robber | Medium |  |  |  | [LC](https://leetcode.com/problems/house-robber/) · [NC](https://neetcode.io/problems/house-robber?list=neetcode150) |
| [ ] | 102 | House Robber II | Medium |  |  |  | [LC](https://leetcode.com/problems/house-robber-ii/) · [NC](https://neetcode.io/problems/house-robber-ii?list=neetcode150) |
| [ ] | 103 | Longest Palindromic Substring | Medium |  |  |  | [LC](https://leetcode.com/problems/longest-palindromic-substring/) · [NC](https://neetcode.io/problems/longest-palindromic-substring?list=neetcode150) |
| [ ] | 104 | Palindromic Substrings | Medium |  |  |  | [LC](https://leetcode.com/problems/palindromic-substrings/) · [NC](https://neetcode.io/problems/palindromic-substrings?list=neetcode150) |
| [ ] | 105 | Decode Ways | Medium |  |  |  | [LC](https://leetcode.com/problems/decode-ways/) · [NC](https://neetcode.io/problems/decode-ways?list=neetcode150) |
| [ ] | 106 | Coin Change | Medium |  |  |  | [LC](https://leetcode.com/problems/coin-change/) · [NC](https://neetcode.io/problems/coin-change?list=neetcode150) |
| [ ] | 107 | Maximum Product Subarray | Medium |  |  |  | [LC](https://leetcode.com/problems/maximum-product-subarray/) · [NC](https://neetcode.io/problems/maximum-product-subarray?list=neetcode150) |
| [ ] | 108 | Word Break | Medium |  |  |  | [LC](https://leetcode.com/problems/word-break/) · [NC](https://neetcode.io/problems/word-break?list=neetcode150) |
| [ ] | 109 | Longest Increasing Subsequence | Medium |  |  |  | [LC](https://leetcode.com/problems/longest-increasing-subsequence/) · [NC](https://neetcode.io/problems/longest-increasing-subsequence?list=neetcode150) |
| [ ] | 110 | Partition Equal Subset Sum | Medium |  |  |  | [LC](https://leetcode.com/problems/partition-equal-subset-sum/) · [NC](https://neetcode.io/problems/partition-equal-subset-sum?list=neetcode150) |

</details>

<details>
<summary><b>2-D Dynamic Programming</b> &nbsp; 0/11</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 111 | Unique Paths | Medium |  |  |  | [LC](https://leetcode.com/problems/unique-paths/) · [NC](https://neetcode.io/problems/count-paths?list=neetcode150) |
| [ ] | 112 | Longest Common Subsequence | Medium |  |  |  | [LC](https://leetcode.com/problems/longest-common-subsequence/) · [NC](https://neetcode.io/problems/longest-common-subsequence?list=neetcode150) |
| [ ] | 113 | Best Time to Buy And Sell Stock With Cooldown | Medium |  |  |  | [LC](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) · [NC](https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown?list=neetcode150) |
| [ ] | 114 | Coin Change II | Medium |  |  |  | [LC](https://leetcode.com/problems/coin-change-ii/) · [NC](https://neetcode.io/problems/coin-change-ii?list=neetcode150) |
| [ ] | 115 | Target Sum | Medium |  |  |  | [LC](https://leetcode.com/problems/target-sum/) · [NC](https://neetcode.io/problems/target-sum?list=neetcode150) |
| [ ] | 116 | Interleaving String | Medium |  |  |  | [LC](https://leetcode.com/problems/interleaving-string/) · [NC](https://neetcode.io/problems/interleaving-string?list=neetcode150) |
| [ ] | 117 | Longest Increasing Path In a Matrix | Hard |  |  |  | [LC](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) · [NC](https://neetcode.io/problems/longest-increasing-path-in-matrix?list=neetcode150) |
| [ ] | 118 | Distinct Subsequences | Hard |  |  |  | [LC](https://leetcode.com/problems/distinct-subsequences/) · [NC](https://neetcode.io/problems/count-subsequences?list=neetcode150) |
| [ ] | 119 | Edit Distance | Medium |  |  |  | [LC](https://leetcode.com/problems/edit-distance/) · [NC](https://neetcode.io/problems/edit-distance?list=neetcode150) |
| [ ] | 120 | Burst Balloons | Hard |  |  |  | [LC](https://leetcode.com/problems/burst-balloons/) · [NC](https://neetcode.io/problems/burst-balloons?list=neetcode150) |
| [ ] | 121 | Regular Expression Matching | Hard |  |  |  | [LC](https://leetcode.com/problems/regular-expression-matching/) · [NC](https://neetcode.io/problems/regular-expression-matching?list=neetcode150) |

</details>

<details>
<summary><b>Greedy</b> &nbsp; 0/8</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 122 | Maximum Subarray | Medium |  |  |  | [LC](https://leetcode.com/problems/maximum-subarray/) · [NC](https://neetcode.io/problems/maximum-subarray?list=neetcode150) |
| [ ] | 123 | Jump Game | Medium |  |  |  | [LC](https://leetcode.com/problems/jump-game/) · [NC](https://neetcode.io/problems/jump-game?list=neetcode150) |
| [ ] | 124 | Jump Game II | Medium |  |  |  | [LC](https://leetcode.com/problems/jump-game-ii/) · [NC](https://neetcode.io/problems/jump-game-ii?list=neetcode150) |
| [ ] | 125 | Gas Station | Medium |  |  |  | [LC](https://leetcode.com/problems/gas-station/) · [NC](https://neetcode.io/problems/gas-station?list=neetcode150) |
| [ ] | 126 | Hand of Straights | Medium |  |  |  | [LC](https://leetcode.com/problems/hand-of-straights/) · [NC](https://neetcode.io/problems/hand-of-straights?list=neetcode150) |
| [ ] | 127 | Merge Triplets to Form Target Triplet | Medium |  |  |  | [LC](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) · [NC](https://neetcode.io/problems/merge-triplets-to-form-target?list=neetcode150) |
| [ ] | 128 | Partition Labels | Medium |  |  |  | [LC](https://leetcode.com/problems/partition-labels/) · [NC](https://neetcode.io/problems/partition-labels?list=neetcode150) |
| [ ] | 129 | Valid Parenthesis String | Medium |  |  |  | [LC](https://leetcode.com/problems/valid-parenthesis-string/) · [NC](https://neetcode.io/problems/valid-parenthesis-string?list=neetcode150) |

</details>

<details>
<summary><b>Intervals</b> &nbsp; 0/6</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 130 | Insert Interval | Medium |  |  |  | [LC](https://leetcode.com/problems/insert-interval/) · [NC](https://neetcode.io/problems/insert-new-interval?list=neetcode150) |
| [ ] | 131 | Merge Intervals | Medium |  |  |  | [LC](https://leetcode.com/problems/merge-intervals/) · [NC](https://neetcode.io/problems/merge-intervals?list=neetcode150) |
| [ ] | 132 | Non Overlapping Intervals | Medium |  |  |  | [LC](https://leetcode.com/problems/non-overlapping-intervals/) · [NC](https://neetcode.io/problems/non-overlapping-intervals?list=neetcode150) |
| [ ] | 133 | Meeting Rooms | Easy |  |  |  | [LC](https://leetcode.com/problems/meeting-rooms/) · [NC](https://neetcode.io/problems/meeting-schedule?list=neetcode150) |
| [ ] | 134 | Meeting Rooms II | Medium |  |  |  | [LC](https://leetcode.com/problems/meeting-rooms-ii/) · [NC](https://neetcode.io/problems/meeting-schedule-ii?list=neetcode150) |
| [ ] | 135 | Minimum Interval to Include Each Query | Hard |  |  |  | [LC](https://leetcode.com/problems/minimum-interval-to-include-each-query/) · [NC](https://neetcode.io/problems/minimum-interval-including-query?list=neetcode150) |

</details>

<details>
<summary><b>Math & Geometry</b> &nbsp; 0/8</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 136 | Rotate Image | Medium |  |  |  | [LC](https://leetcode.com/problems/rotate-image/) · [NC](https://neetcode.io/problems/rotate-matrix?list=neetcode150) |
| [ ] | 137 | Spiral Matrix | Medium |  |  |  | [LC](https://leetcode.com/problems/spiral-matrix/) · [NC](https://neetcode.io/problems/spiral-matrix?list=neetcode150) |
| [ ] | 138 | Set Matrix Zeroes | Medium |  |  |  | [LC](https://leetcode.com/problems/set-matrix-zeroes/) · [NC](https://neetcode.io/problems/set-zeroes-in-matrix?list=neetcode150) |
| [ ] | 139 | Happy Number | Easy |  |  |  | [LC](https://leetcode.com/problems/happy-number/) · [NC](https://neetcode.io/problems/non-cyclical-number?list=neetcode150) |
| [ ] | 140 | Plus One | Easy |  |  |  | [LC](https://leetcode.com/problems/plus-one/) · [NC](https://neetcode.io/problems/plus-one?list=neetcode150) |
| [ ] | 141 | Pow(x, n) | Medium |  |  |  | [LC](https://leetcode.com/problems/powx-n/) · [NC](https://neetcode.io/problems/pow-x-n?list=neetcode150) |
| [ ] | 142 | Multiply Strings | Medium |  |  |  | [LC](https://leetcode.com/problems/multiply-strings/) · [NC](https://neetcode.io/problems/multiply-strings?list=neetcode150) |
| [ ] | 143 | Detect Squares | Medium |  |  |  | [LC](https://leetcode.com/problems/detect-squares/) · [NC](https://neetcode.io/problems/count-squares?list=neetcode150) |

</details>

<details>
<summary><b>Bit Manipulation</b> &nbsp; 0/7</summary>

| | # | Problem | Difficulty | Solution | Conf | Last | Links |
|---|---|---|---|---|---|---|---|
| [ ] | 144 | Single Number | Easy |  |  |  | [LC](https://leetcode.com/problems/single-number/) · [NC](https://neetcode.io/problems/single-number?list=neetcode150) |
| [ ] | 145 | Number of 1 Bits | Easy |  |  |  | [LC](https://leetcode.com/problems/number-of-1-bits/) · [NC](https://neetcode.io/problems/number-of-one-bits?list=neetcode150) |
| [ ] | 146 | Counting Bits | Easy |  |  |  | [LC](https://leetcode.com/problems/counting-bits/) · [NC](https://neetcode.io/problems/counting-bits?list=neetcode150) |
| [ ] | 147 | Reverse Bits | Easy |  |  |  | [LC](https://leetcode.com/problems/reverse-bits/) · [NC](https://neetcode.io/problems/reverse-bits?list=neetcode150) |
| [ ] | 148 | Missing Number | Easy |  |  |  | [LC](https://leetcode.com/problems/missing-number/) · [NC](https://neetcode.io/problems/missing-number?list=neetcode150) |
| [ ] | 149 | Sum of Two Integers | Medium |  |  |  | [LC](https://leetcode.com/problems/sum-of-two-integers/) · [NC](https://neetcode.io/problems/sum-of-two-integers?list=neetcode150) |
| [ ] | 150 | Reverse Integer | Medium |  |  |  | [LC](https://leetcode.com/problems/reverse-integer/) · [NC](https://neetcode.io/problems/reverse-integer?list=neetcode150) |

</details>

---

<sub>Generated by `tools/nc.py readme` on 2026-09-19. Do not edit by hand.</sub>
