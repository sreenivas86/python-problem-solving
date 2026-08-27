Absolutely. For **Level 2: Arrays (71–110)**, the important thing is not just solving each problem. You should learn to recognize **which algorithmic pattern fits the problem**, then understand how to improve from a brute-force solution to an efficient one.

I'll give you for each problem:

* **What the problem asks**
* **Main pattern/method**
* **Brute force → better → best**
* **Typical time complexity**
* **Real-world scenario**
* **What you should learn from it**

> Complexity notation: `n` = number of array elements.

---

# Level 2 — Arrays: Problems 71–110

## 71. Two Sum

### Problem

Given an array of numbers and a target, find two numbers whose sum equals the target.

Example:

`[2, 7, 11, 15]`, target `9`

Answer:

`2 + 7 = 9`

### Methods

**Worst → Best**

1. **Nested loops** → `O(n²)`
2. **Sorting + two pointers** → `O(n log n)`
3. **Hash map** → `O(n)` average

### Pattern

**Hash Map / Complement**

Think:

> "I need `target - current_number`."

### Real-world scenario

Finding two transactions whose combined amount equals a particular payment amount.

---

# 72. Best Time to Buy and Sell Stock

### Problem

Given daily stock prices, buy on one day and sell later to maximize profit.

Example:

`[7, 1, 5, 3, 6, 4]`

Best:

Buy at `1`, sell at `6`.

Profit = `5`

### Methods

1. Try every buy/sell pair → `O(n²)`
2. Track minimum price + maximum profit → **`O(n)`**

### Pattern

**One-pass / Greedy**

Think:

> "What is the cheapest price I've seen so far?"

### Real-world scenario

Determining the best historical buy/sell point for a stock or commodity.

---

# 73. Maximum Subarray

### Problem

Find the contiguous section of an array with the largest sum.

Example:

`[-2,1,-3,4,-1,2,1,-5,4]`

Best subarray:

`[4,-1,2,1]`

Sum = `6`

### Methods

1. Generate every subarray → `O(n²)` or `O(n³)` depending on implementation
2. Prefix sums → `O(n²)`
3. **Kadane's algorithm → O(n)**

### Pattern

**Dynamic Programming / Kadane's Algorithm**

Think:

> "Should I continue the current subarray or start a new one?"

### Real-world scenario

Finding the period with the highest cumulative profit, sales growth, or performance score.

---

# 74. Contains Duplicate

### Problem

Determine whether an array contains repeated values.

Example:

`[1,2,3,1]`

Answer:

**Yes**

### Methods

1. Compare every pair → `O(n²)`
2. Sort → `O(n log n)`
3. **Set → O(n) average**

### Pattern

**Set / Hashing**

### Real-world scenario

Detect duplicate:

* transaction IDs
* user IDs
* order IDs
* file names
* event IDs

---

# 75. Product of Array Except Self

### Problem

For every position, calculate the product of all other elements.

Example:

`[1,2,3,4]`

Result:

`[24,12,8,6]`

### Methods

1. For every element, multiply everything else → `O(n²)`
2. Prefix + suffix products → **`O(n)`**

### Pattern

**Prefix/Suffix**

Important constraint often associated with this problem:

> Don't use division.

### Real-world scenario

Computing a metric for each component based on all other components.

---

# 76. Move Zeroes

### Problem

Move all zeros to the end while maintaining the relative order of non-zero values.

Example:

`[0,1,0,3,12]`

Result:

`[1,3,12,0,0]`

### Methods

1. Repeated shifting → `O(n²)`
2. Extra array → `O(n)` time, `O(n)` space
3. **Two pointers → O(n), O(1) space**

### Pattern

**Two Pointers**

### Real-world scenario

Moving inactive/empty records to the end while keeping active records in order.

---

# 77. Remove Duplicates from Sorted Array

### Problem

Given a **sorted** array, remove duplicates so each value appears once.

Example:

`[1,1,2,2,3]`

Result conceptually:

`[1,2,3]`

### Methods

1. Extra set/array → `O(n)` space
2. **Two pointers → O(n), O(1) space**

### Pattern

**Two Pointers**

### Important clue

The phrase:

> **sorted array**

is a huge hint that a two-pointer technique may work.

---

# 78. Merge Sorted Arrays

### Problem

Combine two already sorted arrays into one sorted array.

Example:

`[1,3,5]`

and

`[2,4,6]`

Result:

`[1,2,3,4,5,6]`

### Methods

1. Combine then sort → `O((n+m) log(n+m))`
2. **Two pointers → O(n+m)**

### Pattern

**Two Pointers / Merge**

### Real-world scenario

Merging two sorted datasets:

* timestamps
* user records
* transaction records
* database results

---

# 79. Plus One

### Problem

An integer is represented as an array of digits.

Example:

`[1,2,3]`

means `123`.

Add one:

`[1,2,4]`

Another:

`[9,9,9]`

becomes:

`[1,0,0,0]`

### Best method

Process digits from **right to left**.

### Pattern

**Carry propagation**

### Complexity

`O(n)`

### Real-world scenario

Incrementing:

* invoice numbers
* counters
* sequence IDs
* numeric identifiers

---

# 80. Majority Element

### Problem

Find the element appearing more than `n/2` times.

Example:

`[2,2,1,1,1,2,2]`

Answer:

`2`

### Methods

1. Frequency dictionary → `O(n)` space
2. Sorting → `O(n log n)`
3. **Boyer-Moore Voting → O(n), O(1)**

### Pattern

**Boyer-Moore Voting**

### Real-world scenario

Finding the dominant category, vote, status, or event type.

---

# 81. Missing Number

### Problem

Array contains numbers from `0` to `n`, with one missing.

Example:

`[3,0,1]`

Missing:

`2`

### Methods

1. Search for every number → `O(n²)`
2. Sort → `O(n log n)`
3. Set → `O(n)` space
4. **Mathematical sum / XOR → O(n), O(1)**

### Pattern

**Mathematical / XOR**

### Real-world scenario

Detecting a missing:

* sequence ID
* record number
* event number

---

# 82. Find All Numbers Disappeared

### Problem

Given numbers from `1` to `n`, find numbers that don't appear.

Example:

`[4,3,2,7,8,2,3,1]`

Missing:

`[5,6]`

### Methods

1. Compare every number → `O(n²)`
2. Set → `O(n)` space
3. **Index marking → O(n), O(1) extra space**

### Pattern

**Array as Hash Map / Index Marking**

### Real-world scenario

Finding missing IDs in a sequence of records.

---

# 83. Rotate Array

### Problem

Move elements around by `k` positions.

Example:

`[1,2,3,4,5]`

Rotate right by `2`:

`[4,5,1,2,3]`

### Methods

1. Rotate one position repeatedly → `O(nk)`
2. Extra array → `O(n)`
3. **Reversal algorithm → O(n), O(1)**

### Pattern

**Array Rotation / Reversal**

You've already worked on left rotation, so this is a very good next step for you.

### Real-world scenario

Rotating:

* scheduling queues
* circular buffers
* time windows
* cyclic workloads

---

# 84. Intersection of Two Arrays

### Problem

Find values appearing in both arrays.

Example:

`[1,2,2,1]`

and

`[2,2]`

Unique intersection:

`[2]`

### Methods

1. Nested loops → `O(n²)`
2. Sorting + two pointers → `O(n log n)`
3. **Set → O(n) average**

### Pattern

**Set / Intersection**

This connects directly to your Level 1 set problem #62.

---

# 85. Third Maximum Number

### Problem

Find the third **distinct** largest number.

Example:

`[3,2,1]`

Answer:

`1`

For:

`[1,2,2,5,3,5]`

Distinct values:

`1,2,3,5`

Third maximum:

`2`

### Methods

1. Sort → `O(n log n)`
2. Set + sorting → `O(n log n)`
3. Track top three values → **O(n)**

### Pattern

**Top K / Tracking**

### Real-world scenario

Finding:

* third-highest salary
* third-largest transaction
* top 3 scores

---

# 86. Maximum Product of Three Numbers

### Problem

Find three numbers whose product is maximum.

Important:

Negative numbers matter.

Example:

`[-10,-10,5,2]`

The maximum can come from:

`-10 × -10 × 5`

### Methods

1. Check every combination → `O(n³)`
2. Sort → `O(n log n)`
3. Track largest and smallest values → **O(n)**

### Pattern

**Top/Bottom extremes**

### Important lesson

Don't assume:

> "Only the three largest numbers matter."

Two negative numbers can produce a large positive product.

---

# 87. Height Checker

### Problem

Students have heights in an order. Find how many are not in the expected sorted order.

Example:

Actual:

`[1,1,4,2,1,3]`

Expected sorted:

`[1,1,1,2,3,4]`

Compare positions and count mismatches.

### Methods

1. Sort a copy → `O(n log n)`
2. Counting sort when height range is small → **O(n + k)**

### Pattern

**Sorting / Counting**

### Real-world scenario

Checking whether records are in expected order.

---

# 88. Sort Array by Parity

### Problem

Move even numbers and odd numbers into separate sections.

Example:

`[3,1,2,4]`

Possible result:

`[2,4,3,1]`

### Methods

1. Sorting → `O(n log n)`
2. Extra arrays → `O(n)`
3. **Two pointers → O(n), O(1)**

### Pattern

**Partition / Two Pointers**

### Real-world scenario

Separating:

* valid/invalid records
* active/inactive items
* priority/non-priority records

---

# 89. Squares of Sorted Array

### Problem

Given a sorted array that may contain negative numbers, return squares in sorted order.

Example:

`[-4,-1,0,3,10]`

Squares:

`[16,1,0,9,100]`

Sorted:

`[0,1,9,16,100]`

### Methods

1. Square everything + sort → `O(n log n)`
2. **Two pointers → O(n)**

### Pattern

**Two Pointers**

Important observation:

The largest square comes from either:

**leftmost negative**

or

**rightmost positive**

---

# 90. Pivot Index

### Problem

Find an index where:

**sum of elements on the left = sum of elements on the right**

Example:

`[1,7,3,6,5,6]`

Pivot index:

`3`

Left:

`1+7+3 = 11`

Right:

`5+6 = 11`

### Methods

1. Calculate left/right sums repeatedly → `O(n²)`
2. Prefix sums → `O(n)` but extra space
3. **Total sum + running left sum → O(n), O(1)**

### Pattern

**Prefix Sum**

### Real-world scenario

Finding a balance point in:

* workload
* revenue
* resource allocation

---

# 91. Running Sum

### Problem

Each position contains the sum of all previous values including itself.

Example:

`[1,2,3,4]`

Running sum:

`[1,3,6,10]`

### Method

**One pass → O(n)**

### Pattern

**Prefix / Running Sum**

### Real-world scenario

Cumulative:

* sales
* expenses
* traffic
* transactions
* resource usage

---

# 92. Richest Customer Wealth

### Problem

Each row represents a customer, and each value represents money in an account.

Find the customer with the largest total wealth.

Example:

```text
Customer 1 → 1 + 2 + 3 = 6
Customer 2 → 3 + 2 + 1 = 6
```

Maximum wealth = `6`

### Method

Calculate each row's sum.

**O(rows × accounts)**

### Pattern

**2D Array + Aggregation**

### Real-world scenario

Finding the customer with the highest total account balance.

---

# 93. Kids With Greatest Candies

### Problem

For every child, determine whether giving them some extra candies would make them have the greatest number.

### Pattern

**Maximum + comparison**

First determine the current maximum.

Then compare each child after adding the extra candies.

### Complexity

`O(n)`

### Real-world scenario

Testing whether adding resources would make each team/person reach the highest level.

---

# 94. Shuffle Array

### Problem

Randomly rearrange elements.

Example:

`[1,2,3,4]`

could become:

`[3,1,4,2]`

### Important method

**Fisher-Yates shuffle**

### Complexity

**O(n)**

### Real-world scenario

* Random sampling
* Random task assignment
* Card shuffling
* Training-data randomization

---

# 95. Build Array from Permutation

### Problem

Given an array representing indexes, construct a new array by using each value as an index.

Example:

`nums = [0,2,1,5,3,4]`

The output uses:

`nums[nums[i]]`

### Pattern

**Index Mapping**

### Complexity

`O(n)`

### Real-world scenario

Reordering records according to an index mapping.

---

# 96. Concatenation of Array

### Problem

Given:

`[1,2,3]`

Concatenate it with itself:

`[1,2,3,1,2,3]`

### Method

Simple array construction.

### Complexity

`O(n)`

### Real-world scenario

Repeating a schedule, pattern, or sequence.

---

# 97. Duplicate Zeros

### Problem

Whenever you encounter zero, duplicate it while keeping the array's fixed length.

Example:

`[1,0,2,3,0,4,5,0]`

becomes conceptually:

`[1,0,0,2,3,0,0,4]`

### Methods

1. Extra array → `O(n)` space
2. In-place shifting → potentially `O(n²)`
3. **Two-pointer/counting approach → O(n), O(1)**

### Pattern

**Two Pointers / In-place manipulation**

### Real-world scenario

Expanding special events in a fixed-size buffer.

---

# 98. Spiral Matrix

### Problem

Traverse a matrix in spiral order.

Example:

```text
1 2 3
4 5 6
7 8 9
```

Spiral:

`1 → 2 → 3 → 6 → 9 → 8 → 7 → 4 → 5`

### Pattern

**Boundary Traversal**

Maintain:

* top
* bottom
* left
* right

### Complexity

`O(m × n)`

### Real-world scenario

Processing matrix/grid data layer by layer.

---

# 99. Rotate Matrix

### Problem

Rotate a square matrix, commonly by 90 degrees clockwise.

Example:

```text
1 2 3
4 5 6
7 8 9
```

becomes:

```text
7 4 1
8 5 2
9 6 3
```

### Methods

1. Extra matrix → `O(n²)` space
2. **Transpose + reverse → O(n²), O(1) extra space**

### Pattern

**Matrix Transformation**

### Real-world scenario

Image rotation, grid transformations, spatial data.

---

# 100. Set Matrix Zeroes

### Problem

If any cell is zero, make its entire row and column zero.

Example:

```text
1 1 1
1 0 1
1 1 1
```

becomes:

```text
1 0 1
0 0 0
1 0 1
```

### Methods

1. Additional matrix → `O(mn)` space
2. Row/column sets → `O(m+n)` space
3. **Use matrix's first row/column as markers → O(1) extra space**

### Pattern

**In-place marking**

### Real-world scenario

Data-quality propagation: if a particular cell indicates invalid data, invalidate its related row/column.

---

# 101. Merge Intervals

### Problem

Given intervals, merge overlapping intervals.

Example:

`[1,3] [2,6] [8,10]`

becomes:

`[1,6] [8,10]`

### Methods

1. Brute-force comparison → potentially `O(n²)`
2. **Sort by start + merge → O(n log n)**

### Pattern

**Intervals + Sorting**

### Real-world scenario

Merging:

* employee schedules
* server downtime
* booking periods
* network maintenance windows

---

# 102. Insert Interval

### Problem

You have sorted, non-overlapping intervals and need to insert a new interval while maintaining those properties.

Example:

Existing:

`[1,3] [6,9]`

Insert:

`[2,5]`

Result:

`[1,5] [6,9]`

### Methods

1. Insert then merge/sort → `O(n log n)`
2. **Linear scan → O(n)**

### Pattern

**Intervals + Merge**

### Real-world scenario

Adding a new:

* booking
* maintenance window
* meeting
* reservation

---

# 103. Summary Ranges

### Problem

Convert consecutive numbers into compact ranges.

Example:

`[0,1,2,4,5,7]`

becomes:

`0-2, 4-5, 7`

### Pattern

**Consecutive sequence detection**

### Complexity

`O(n)`

### Real-world scenario

Summarizing:

* available dates
* IP ranges
* server IDs
* sequence numbers

---

# 104. Missing Ranges

### Problem

Given a range and some existing numbers, find the missing ranges.

Example:

Range:

`0–10`

Existing:

`[0,1,3,50,75]`

Depending on bounds, identify gaps such as:

`2`

`4–10`

### Pattern

**Gap Detection**

### Real-world scenario

Finding missing:

* transaction IDs
* dates
* sequence numbers
* log events

---

# 105. Maximum Average Subarray

### Problem

Find the contiguous subarray of exactly `k` elements with the highest average.

Example:

`[1,12,-5,-6,50,3]`

with `k = 4`

Find the 4-element window with maximum average.

### Methods

1. Calculate every window from scratch → `O(nk)`
2. **Sliding Window → O(n)**

### Pattern

**Fixed-size Sliding Window**

### Real-world scenario

Finding the highest average:

* CPU usage over a fixed period
* network traffic
* sales over 7 days
* sensor readings

---

# 106. Longest Consecutive Sequence

### Problem

Find the longest sequence of consecutive integers.

Example:

`[100,4,200,1,3,2]`

Longest:

`1,2,3,4`

Length = `4`

### Methods

1. Sort → `O(n log n)`
2. **Set → O(n) average**

### Pattern

**Hash Set + Sequence Detection**

### Real-world scenario

Finding longest continuous:

* transaction sequence
* daily activity streak
* ID sequence
* system uptime sequence

---

# 107. Subarray Sum Equals K

### Problem

Find how many contiguous subarrays have a sum equal to `k`.

Example:

`[1,1,1]`

`k = 2`

Subarrays:

`[1,1]`

`[1,1]`

Answer:

`2`

### Methods

1. Generate all subarrays → `O(n²)`
2. Prefix sum + hash map → **O(n)**

### Pattern

**Prefix Sum + Hash Map**

This is an important interview pattern.

### Real-world scenario

Finding continuous periods where:

* revenue equals a target
* transactions total a target
* resource usage reaches a target

---

# 108. Maximum Circular Subarray

### Problem

Find the maximum subarray when the array is considered **circular**.

Example:

The end and beginning can connect.

So:

`[5,-3,5]`

can use:

`5 + 5 = 10`

### Methods

1. Brute force → `O(n²)`
2. **Kadane + total sum/minimum subarray → O(n)**

### Pattern

**Kadane + Circular Array**

### Real-world scenario

Circular scheduling, cyclic workloads, repeating time periods.

---

# 109. Gas Station

### Problem

You have gas stations arranged in a circle.

Each station provides gas and requires gas to travel to the next station.

Find where you can start and complete the full circle.

### Methods

1. Try every starting station → `O(n²)`
2. **Greedy → O(n)**

### Pattern

**Greedy**

Important idea:

If your current fuel becomes negative, that starting position cannot work.

### Real-world scenario

Finding a viable starting point in:

* circular delivery routes
* vehicle routes
* resource cycles
* machine processing cycles

---

# 110. Jump Game

### Problem

Each number tells you the maximum distance you can jump from that position.

Example:

`[2,3,1,1,4]`

You can reach the last position.

### Methods

1. Recursive exploration → exponential
2. Dynamic Programming → `O(n²)`
3. **Greedy → O(n)**

### Pattern

**Greedy / Reachability**

Think:

> "What is the furthest position I can reach so far?"

### Real-world scenario

Determining whether:

* a workflow can reach its final stage
* a deployment pipeline can progress
* a network process can reach a destination
* tasks can be completed given resource limits

---

# 🧠 The Most Important Part: Pattern Recognition

Don't try to memorize 40 solutions.

Learn these patterns.

| Pattern                    | Problems                        |
| -------------------------- | ------------------------------- |
| **Hash Map**               | 71, 80, 107                     |
| **Hash Set**               | 74, 84, 106                     |
| **Two Pointers**           | 76, 77, 78, 88, 89, 97          |
| **Sliding Window**         | 105                             |
| **Prefix Sum**             | 90, 91, 107                     |
| **Kadane's Algorithm**     | 73, 108                         |
| **Greedy**                 | 72, 109, 110                    |
| **Sorting**                | 78, 85, 87, 101                 |
| **Intervals**              | 101, 102                        |
| **Matrix Traversal**       | 98, 99, 100                     |
| **Index Manipulation**     | 82, 95                          |
| **Math / XOR**             | 81                              |
| **Top K / Extremes**       | 85, 86                          |
| **In-place Array**         | 76, 77, 88, 97, 100             |
| **Running/Prefix Sum**     | 90, 91                          |
| **Partition**              | 88                              |
| **Backtracking/Recursion** | Mostly not required in this set |

---

# ⭐ Worst → Best Thinking

When you solve these problems, use this progression:

### Level 1 — Brute Force

Ask:

> "Can I solve this by checking every possibility?"

Usually:

**O(n²)** or worse.

This is important because it helps you understand the problem.

---

### Level 2 — Improve using Sorting

Ask:

> "If I sort the data, does the problem become easier?"

Usually:

**O(n log n)**

Examples:

* Two Sum
* Merge arrays
* Third maximum
* Intervals

---

### Level 3 — Hashing

Ask:

> "Can I remember things I've already seen?"

Usually:

**O(n)** average.

Examples:

* Two Sum
* Contains Duplicate
* Longest Consecutive Sequence
* Subarray Sum

---

### Level 4 — Two Pointers

Ask:

> "Can I process the array from two directions or maintain two positions?"

Usually:

**O(n)**.

Examples:

* Move Zeroes
* Remove Duplicates
* Merge Sorted Arrays
* Squares of Sorted Array

---

### Level 5 — Sliding Window

Ask:

> "Am I dealing with a contiguous section of the array?"

Especially when you see:

* subarray
* consecutive elements
* exactly `k` elements
* maximum/minimum over a window

Think:

**Sliding Window**

Example:

**105. Maximum Average Subarray**

---

### Level 6 — Prefix Sum

Ask:

> "Do I repeatedly need sums of portions of the array?"

Think:

**Prefix Sum**

Examples:

* Pivot Index
* Running Sum
* Subarray Sum Equals K

---

### Level 7 — Greedy

Ask:

> "Can I make the best local decision while guaranteeing the overall result?"

Examples:

* Stock
* Gas Station
* Jump Game

---

# 🎯 What I Recommend You Learn in Order

Don't learn these 40 randomly.

For your Python/Data Engineering preparation, I'd learn them in this order:

### Phase 1 — Basic Array Operations

**76 → 79 → 91 → 92 → 93 → 94 → 95 → 96**

Understand array traversal and manipulation.

### Phase 2 — Sets & Hash Maps

**74 → 71 → 81 → 84 → 106**

Learn how arrays interact with dictionaries and sets.

### Phase 3 — Two Pointers

**76 → 77 → 78 → 88 → 89**

This is a very important pattern.

### Phase 4 — Prefix Sum

**90 → 91 → 107**

Learn cumulative calculations.

### Phase 5 — Sliding Window

**105**

Then apply the same concept to other subarray problems.

### Phase 6 — Kadane

**73 → 108**

Learn maximum-subarray thinking.

### Phase 7 — Sorting & Intervals

**85 → 87 → 101 → 102 → 103 → 104**

Very useful for real-world data processing.

### Phase 8 — Matrix

**98 → 99 → 100**

Learn 2D-array manipulation.

### Phase 9 — Greedy

**72 → 109 → 110**

Learn optimization without exploring every possibility.

---

# 🔥 The 10 Patterns I Would Prioritize

For your current learning stage, these are the most valuable:

1. **Hash Map**
2. **Hash Set**
3. **Two Pointers**
4. **Sliding Window**
5. **Prefix Sum**
6. **Kadane's Algorithm**
7. **Sorting**
8. **Greedy**
9. **Intervals**
10. **Matrix Traversal**

Once you recognize these patterns, a problem like:

> "Find duplicate records"

immediately makes you think **Set**.

> "Find two values matching a target"

→ **Hash Map / Two Sum**

> "Find maximum sum of consecutive values"

→ **Kadane / Sliding Window depending on constraints**

> "Find maximum average for exactly K consecutive values"

→ **Sliding Window**

> "Find common records between datasets"

→ **Set Intersection**

> "Merge overlapping time periods"

→ **Sort + Intervals**

That **pattern recognition** is much more important than memorizing individual solutions.
-------------------------------------------------------------
