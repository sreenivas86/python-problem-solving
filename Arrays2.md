Yes. For **Problems 71–110**, I recommend learning them as **Python problem-solving patterns**, not as 40 separate programs.

Below is a detailed guide showing **what to think about, which Python tools/data structures to consider, and how the approaches improve from brute force to optimal**. No code for now.

---

# Level 2: Arrays — Detailed Python Guide

## First: Python tools you should know

Before starting these problems, become comfortable with:

| Python feature            | Use                          |
| ------------------------- | ---------------------------- |
| `list`                    | General array operations     |
| `set`                     | Uniqueness / membership      |
| `dict`                    | Frequency / lookup / mapping |
| `enumerate()`             | Index + value                |
| `range()`                 | Index-based traversal        |
| `len()`                   | Array size                   |
| `sorted()`                | Return a sorted copy         |
| `.sort()`                 | Sort list in-place           |
| `sum()`                   | Calculate total              |
| `min()` / `max()`         | Minimum / maximum            |
| `append()`                | Add element                  |
| `pop()`                   | Remove element               |
| `reversed()`              | Reverse traversal            |
| `zip()`                   | Process multiple sequences   |
| `collections.Counter`     | Frequency counting           |
| `collections.defaultdict` | Grouping                     |
| `math`                    | Mathematical calculations    |

For interviews, however, **don't blindly use built-ins**. First understand the algorithm.

---

# 71. Two Sum

### Problem

Given:

`[2, 7, 11, 15]`

and target:

`9`

Find two numbers whose sum is `9`.

Answer:

`2 + 7 = 9`

### Method 1 — Brute Force

Compare every number with every other number.

### Complexity

**Time:** `O(n²)`
**Space:** `O(1)`

### Method 2 — Sorting + Two Pointers

Sort the array.

Then use:

* one pointer at the beginning
* one pointer at the end

If the sum is too small → move left pointer.

If the sum is too large → move right pointer.

### Complexity

**Time:** `O(n log n)`
**Space:** depends on sorting/implementation.

### Method 3 — Dictionary ⭐

For every number, calculate:

**target − current number**

Check whether that value has already been seen.

### Complexity

**Time:** `O(n)` average
**Space:** `O(n)`

### Python method to learn

**Dictionary**

### Pattern

**Hash Map / Complement**

---

# 72. Best Time to Buy and Sell Stock

### Problem

Prices:

`[7,1,5,3,6,4]`

You need:

**maximum profit**

Buy at `1`.

Sell at `6`.

Profit:

`5`

### Brute force

Try every possible buy/sell combination.

**O(n²)**

### Better method

Keep track of:

* minimum price seen so far
* maximum profit so far

You only need one pass.

### Complexity

**O(n)** time
**O(1)** space

### Python concept

Simple variables + loop.

### Pattern

**Greedy / One Pass**

---

# 73. Maximum Subarray

### Problem

Find the contiguous section with the largest sum.

Example:

`[-2,1,-3,4,-1,2,1,-5,4]`

Best:

`[4,-1,2,1]`

Sum:

`6`

### Brute force

Generate every possible subarray.

Can become:

**O(n²)** or **O(n³)**.

### Best method

**Kadane's Algorithm**

At every position ask:

> Should I continue the current subarray or start a new one here?

### Complexity

**O(n)** time
**O(1)** space

### Python concept

Running variables.

### Pattern

**Dynamic Programming / Kadane**

---

# 74. Contains Duplicate

### Problem

`[1,2,3,1]`

Does any value appear more than once?

Answer:

**Yes**

### Brute force

Compare every pair.

**O(n²)**

### Better

Sort first.

**O(n log n)**

### Best practical method

Use a `set`.

A set only keeps unique values.

### Complexity

**O(n)** average time
**O(n)** space

### Python method

`set`

### Pattern

**Hash Set**

---

# 75. Product of Array Except Self

### Problem

Input:

`[1,2,3,4]`

Output:

`[24,12,8,6]`

For every position, multiply everything except itself.

### Brute force

For every element, loop through the entire array.

**O(n²)**

### Better

Use prefix and suffix products.

Concept:

```text
left product × right product
```

For every position.

### Complexity

**O(n)** time.

### Python concept

Lists + running products.

### Pattern

**Prefix / Suffix**

---

# 76. Move Zeroes

### Problem

Input:

`[0,1,0,3,12]`

Output:

`[1,3,12,0,0]`

The relative order of non-zero elements should remain the same.

### Methods

#### Brute force

Repeatedly remove/move zeros.

Potentially **O(n²)**.

#### Extra list

Create a new list.

**O(n)** time
**O(n)** space

#### Two pointers ⭐

Keep track of where the next non-zero element should go.

**O(n)** time
**O(1)** extra space

### Python concept

List + two indexes.

### Pattern

**Two Pointers / In-place**

---

# 77. Remove Duplicates from Sorted Array

### Important clue

The array is already **sorted**.

Example:

`[1,1,2,2,3]`

Result:

`[1,2,3]`

Because equal values are next to each other.

### Method

Use two positions:

* one tracks the unique portion
* another scans the array

### Complexity

**O(n)** time
**O(1)** space

### Pattern

**Two Pointers**

### Python concept

List indexing.

---

# 78. Merge Sorted Arrays

Given:

`[1,3,5]`

and:

`[2,4,6]`

Produce:

`[1,2,3,4,5,6]`

### Brute force

Combine and sort.

**O(n log n)**

### Best

Two pointers.

Compare the current values from both arrays.

Take the smaller one and advance that pointer.

### Complexity

**O(n + m)**

### Pattern

**Two Pointers / Merge**

### Real-world connection

This is basically the idea behind the **merge phase of merge sort**.

---

# 79. Plus One

### Problem

`[1,2,3]`

represents `123`.

Add one:

`[1,2,4]`

But:

`[9,9,9]`

becomes:

`[1,0,0,0]`

### Best method

Start from the rightmost digit.

Handle the carry.

### Complexity

**O(n)** worst case.

### Pattern

**Carry Propagation**

### Python concepts

List indexing from the end.

---

# 80. Majority Element

### Problem

Find an element appearing more than `n/2` times.

Example:

`[2,2,1,1,1,2,2]`

Answer:

`2`

### Methods

**Frequency dictionary**

`O(n)` time
`O(n)` space

**Sorting**

`O(n log n)`

**Boyer-Moore**

`O(n)` time
`O(1)` space ⭐

### Python concept

Dictionary first, then learn Boyer-Moore.

### Pattern

**Frequency → Voting**

---

# 81. Missing Number

Numbers should contain:

`0 → n`

but one is missing.

Example:

`[3,0,1]`

Missing:

`2`

### Methods

#### Sorting

`O(n log n)`

#### Set

`O(n)` time + `O(n)` space

#### Mathematical sum

Expected sum minus actual sum.

`O(n)` time
`O(1)` space

#### XOR

Another `O(n)` / `O(1)` technique.

### Python concept

Arithmetic first; understand XOR afterward.

### Pattern

**Math / XOR**

---

# 82. Find All Numbers Disappeared

Example:

`[4,3,2,7,8,2,3,1]`

Numbers from `1` to `8`.

Missing:

`5,6`

### Methods

Set:

**O(n)** space.

### Better interview technique

Use the array indexes themselves as markers.

**O(n)** time
**O(1)** extra space.

### Pattern

**Index Marking**

This is an important interview technique.

---

# 83. Rotate Array

Example:

`[1,2,3,4,5]`

Rotate right by 2:

`[4,5,1,2,3]`

### Methods

Repeated rotation:

**O(nk)**

Extra list:

**O(n)** space

Reversal:

**O(n)** time
**O(1)** space ⭐

### Python concept

List slicing is convenient, but learn the **reversal algorithm** because it teaches array manipulation.

### Pattern

**Array Rotation / Reversal**

---

# 84. Intersection of Two Arrays

Find values appearing in both.

A:

`[1,2,2,1]`

B:

`[2,2]`

Unique intersection:

`[2]`

### Methods

Nested loops:

**O(n²)**

Sort + two pointers:

**O(n log n)**

Set:

**O(n)** average.

### Python method

`set`

### Pattern

**Set Intersection**

This directly connects with your earlier **#62 Intersection** problem.

---

# 85. Third Maximum Number

Find the third distinct largest value.

Example:

`[3,2,1]`

Answer:

`1`

### Methods

Sort:

**O(n log n)**

Set + sort:

**O(n log n)**

Track top three:

**O(n)** ⭐

### Python concept

Maintain the largest three distinct values.

### Pattern

**Top K / Tracking**

---

# 86. Maximum Product of Three Numbers

Need three numbers with maximum product.

### Important

Negative values matter.

Example:

`[-10,-10,5,2]`

`(-10 × -10 × 5) = 500`

### Key observation

The answer comes from one of:

* three largest values
* two smallest values × largest value

### Method

Sort:

**O(n log n)**

Track extremes:

**O(n)**

### Pattern

**Extreme Values**

---

# 87. Height Checker

Given actual heights, determine how many are not in their expected sorted positions.

### Method

Create sorted expected order.

Compare original and sorted positions.

### Complexity

Normal sorting:

**O(n log n)**

If the height range is small:

**Counting sort → O(n + k)**

### Pattern

**Sorting / Counting**

---

# 88. Sort Array by Parity

Put even values before odd values.

Example:

`[3,1,2,4]`

Possible result:

`[2,4,3,1]`

### Methods

Create separate lists:

**O(n)** space

Two pointers:

**O(n)** time
**O(1)** extra space

### Pattern

**Partition / Two Pointers**

---

# 89. Squares of Sorted Array

Input:

`[-4,-1,0,3,10]`

Output:

`[0,1,9,16,100]`

### Important observation

The largest square can come from either end.

Why?

`-4² = 16`

`10² = 100`

So compare the absolute values at both ends.

### Method

Two pointers.

**O(n)** time.

### Pattern

**Two Pointers**

---

# 90. Pivot Index

Find an index where:

**left sum = right sum**

Example:

`[1,7,3,6,5,6]`

Pivot:

`3`

### Best approach

Calculate total sum first.

Then maintain a running left sum.

Right sum can be calculated as:

**total − left − current**

### Complexity

**O(n)** time
**O(1)** space

### Pattern

**Prefix Sum / Running Sum**

---

# 91. Running Sum

Input:

`[1,2,3,4]`

Output:

`[1,3,6,10]`

### Method

Keep a running total.

### Complexity

**O(n)**

### Pattern

**Prefix Sum**

This is one of the easiest problems for learning prefix sums.

---

# 92. Richest Customer Wealth

2D array:

```text
Customer 1 → [1,2,3]
Customer 2 → [3,2,1]
```

Calculate each customer's total.

### Method

For each row:

**sum the row**

Then find maximum.

### Complexity

**O(m × n)**

### Python methods

`sum()`

`max()`

### Pattern

**2D Array + Aggregation**

---

# 93. Kids With Greatest Candies

Given:

* candies for each child
* extra candies

Determine whether each child could become the child with the most candies.

### Method

First find:

**current maximum**

Then for every child:

**current candies + extra**

Compare against maximum.

### Complexity

**O(n)**

### Pattern

**Maximum + Comparison**

---

# 94. Shuffle Array

Randomly rearrange elements.

### Don't use a naive random swap approach.

The algorithm you should learn is:

**Fisher-Yates Shuffle**

### Complexity

**O(n)**

### Python

Python's `random` module has tools for randomization, but understand Fisher-Yates first.

### Real-world

* Shuffle cards
* Random task allocation
* Randomized datasets
* ML training data

---

# 95. Build Array from Permutation

This is mainly about **index manipulation**.

If:

`nums = [0,2,1,5,3,4]`

you construct the result by treating values as indexes.

### Pattern

**Array as index mapping**

### Complexity

**O(n)**

### Important

Understand:

> A value can represent the position of another value.

This concept appears frequently in array problems.

---

# 96. Concatenation of Array

Given:

`[1,2,3]`

return:

`[1,2,3,1,2,3]`

### Method

Simple list operation.

### Complexity

**O(n)**

### Python

List concatenation/repetition.

### Difficulty

⭐ Easy.

This is mainly to make you comfortable with Python lists.

---

# 97. Duplicate Zeros

Whenever you see zero, duplicate it while maintaining fixed array size.

### Example

Input:

`[1,0,2,3,0,4,5,0]`

Output:

`[1,0,0,2,3,0,0,4]`

### Methods

Extra list:

**O(n)** space

In-place shifting:

can become **O(n²)**

Optimized two-pointer technique:

**O(n)** time
**O(1)** space

### Pattern

**Two Pointers / In-place**

---

# 98. Spiral Matrix

Matrix:

```text
1 2 3
4 5 6
7 8 9
```

Output:

`1,2,3,6,9,8,7,4,5`

### Pattern

Maintain four boundaries:

* top
* bottom
* left
* right

Move around the outside and shrink the boundaries.

### Complexity

**O(m × n)**

### Python

2D list indexing.

---

# 99. Rotate Matrix

Rotate matrix 90° clockwise.

### Best method

Two conceptual operations:

**Transpose**

then

**Reverse each row**

### Complexity

**O(n²)**

### Space

**O(1)** extra space if done in-place.

### Pattern

**Matrix Transformation**

---

# 100. Set Matrix Zeroes

If one element is zero, its entire row and column become zero.

### Methods

Extra matrix:

**O(mn)** space

Row/column sets:

**O(m+n)** space

Use first row/column as markers:

**O(1)** space ⭐

### Pattern

**In-place Marking**

This is a more advanced array problem.

---

# 101. Merge Intervals

Input:

`[1,3], [2,6], [8,10]`

Output:

`[1,6], [8,10]`

### First step

Sort intervals by starting position.

### Then

Compare current interval with previous merged interval.

If they overlap → merge.

### Complexity

**O(n log n)** because of sorting.

### Pattern

**Sorting + Intervals**

### Real-world

Very important:

* meetings
* reservations
* server downtime
* maintenance windows
* employee schedules

---

# 102. Insert Interval

Existing:

`[1,3], [6,9]`

New:

`[2,5]`

Result:

`[1,5], [6,9]`

### Pattern

**Insert + Merge**

Because the intervals are already sorted, you can solve it in:

**O(n)**

without sorting everything again.

---

# 103. Summary Ranges

Input:

`[0,1,2,4,5,7]`

Output conceptually:

`0-2`

`4-5`

`7`

### Pattern

**Consecutive sequence detection**

### Complexity

**O(n)**

### Real-world

Summarizing:

`1001,1002,1003,1005,1006`

as:

`1001–1003, 1005–1006`

---

# 104. Missing Ranges

Given:

**lower bound + upper bound + existing numbers**

find the missing portions.

### Pattern

**Gap Detection**

You compare the current number with the previous number.

If there is a gap, generate that missing range.

### Complexity

Usually:

**O(n)**

### Real-world

Excellent example for:

* missing IDs
* missing dates
* missing sequence numbers
* incomplete logs

---

# 105. Maximum Average Subarray

Given an array and `k`.

Find the consecutive `k` elements with maximum average.

### Brute force

Calculate every window from scratch.

**O(nk)**

### Best

Sliding Window.

Instead of recalculating:

```text
new window sum
```

from scratch, remove the value leaving the window and add the value entering it.

### Complexity

**O(n)**

### Pattern

⭐⭐⭐⭐⭐ **Sliding Window**

This is a very important pattern.

---

# 106. Longest Consecutive Sequence

Input:

`[100,4,200,1,3,2]`

Longest sequence:

`1,2,3,4`

Length:

`4`

### Sorting method

Sort:

`[1,2,3,4,100,200]`

Then scan.

**O(n log n)**

### Better

Put everything in a set.

For each number, ask:

> Does `number - 1` exist?

If not, it might be the start of a sequence.

Then continue forward.

### Complexity

**O(n)** average.

### Pattern

**Set + Sequence Detection**

---

# 107. Subarray Sum Equals K

Find the number of contiguous subarrays whose sum equals `k`.

Example:

`[1,1,1]`

k = `2`

Answer:

`2`

### Brute force

Try every subarray.

**O(n²)**

### Best

Use:

**Prefix Sum + Dictionary**

This is an important advanced pattern.

### Concept

If:

`current_prefix - previous_prefix = k`

then the section between those positions has sum `k`.

### Complexity

**O(n)** average.

### Pattern

⭐⭐⭐⭐⭐ **Prefix Sum + Hash Map**

---

# 108. Maximum Circular Subarray

Normally, maximum subarray cannot wrap around.

Here it can.

Example:

`[5,-3,5]`

Normal maximum:

`7`

Circular maximum:

`10`

because the first and last `5` can connect.

### Best method

Use:

**Kadane's algorithm**

plus

**minimum subarray calculation**

and total sum.

### Complexity

**O(n)**

### Pattern

**Kadane + Circular Array**

---

# 109. Gas Station

You have:

**gas available**

and

**gas required to travel**

around a circle.

Find a starting station that allows you to complete the entire route.

### Brute force

Try every station.

**O(n²)**

### Greedy

Track:

* total gas balance
* current balance
* current starting point

If current balance becomes negative, the current starting point cannot work.

### Complexity

**O(n)**

### Pattern

⭐⭐⭐⭐⭐ **Greedy**

---

# 110. Jump Game

Each value represents the maximum jump length.

Example:

`[2,3,1,1,4]`

You can reach the end.

### Brute force

Explore every possible jump.

Potentially exponential.

### Dynamic Programming

Track whether each position is reachable.

Can be:

**O(n²)**

### Greedy ⭐

Track the furthest reachable position.

If your current index exceeds that reach, you cannot continue.

### Complexity

**O(n)** time
**O(1)** space

### Pattern

**Greedy / Reachability**

---

# 🚀 Your Python Method Roadmap

I recommend learning the problems in this order rather than simply 71 → 110.

## Phase 1 — Basic List Thinking

Learn:

* 76 Move Zeroes
* 79 Plus One
* 91 Running Sum
* 92 Richest Customer
* 93 Kids With Greatest Candies
* 96 Concatenation

Python skills:

**list + loop + indexing + `sum()` + `max()`**

---

## Phase 2 — Set / Dictionary

Learn:

* 71 Two Sum
* 74 Contains Duplicate
* 80 Majority Element
* 81 Missing Number
* 84 Intersection
* 106 Longest Consecutive

Python:

**`dict` + `set`**

This connects directly with the dictionary/set problems you just completed.

---

## Phase 3 — Two Pointers

Learn:

* 77 Remove Duplicates
* 78 Merge Sorted Arrays
* 88 Sort by Parity
* 89 Squares of Sorted Array
* 97 Duplicate Zeros

Main idea:

**left pointer + right pointer**

This is one of the most important patterns for you.

---

## Phase 4 — Prefix Sum

Learn:

* 90 Pivot Index
* 91 Running Sum
* 107 Subarray Sum Equals K

Start with simple running sums and progress toward:

**Prefix Sum + Dictionary**

---

## Phase 5 — Sliding Window

Learn:

* 105 Maximum Average Subarray

Then understand the general pattern:

**Add incoming → remove outgoing → maintain window**

---

## Phase 6 — Kadane

Learn:

* 73 Maximum Subarray
* 108 Maximum Circular Subarray

Understand normal Kadane first.

Then circular Kadane.

---

## Phase 7 — Sorting + Intervals

Learn:

* 85 Third Maximum
* 87 Height Checker
* 101 Merge Intervals
* 102 Insert Interval
* 103 Summary Ranges
* 104 Missing Ranges

This is particularly useful for real-world data processing.

---

## Phase 8 — Matrix

Learn:

* 98 Spiral Matrix
* 99 Rotate Matrix
* 100 Set Matrix Zeroes

These improve your 2D-array skills.

---

## Phase 9 — Greedy

Finally:

* 72 Stock
* 109 Gas Station
* 110 Jump Game

These teach you how to avoid brute-force exploration.

---

# ⭐ Worst → Best Strategy

For **every problem**, train yourself to ask these questions in order:

### 1. Can I brute-force it?

Usually:

`O(n²)` or worse.

Don't be afraid of this approach. It helps you understand the problem.

### 2. Can sorting simplify it?

Often:

`O(n log n)`

Look for:

* sorted data
* ordering
* intervals
* duplicates
* top/bottom values

### 3. Can a `set` help?

Ask:

> "Do I just need to know whether I've seen this value?"

Think:

**Set**

### 4. Can a `dict` help?

Ask:

> "Do I need to remember information about a value?"

Think:

**Dictionary**

Examples:

`value → index`

`value → count`

`prefix_sum → frequency`

### 5. Can two pointers help?

Look for:

* sorted arrays
* moving from both ends
* removing duplicates
* merging
* partitioning

### 6. Is this a contiguous subarray?

Think:

**Sliding Window** or **Prefix Sum**

### 7. Am I repeatedly calculating sums?

Think:

**Prefix Sum**

### 8. Am I finding maximum contiguous sum?

Think:

**Kadane**

### 9. Can I make a local optimal decision?

Think:

**Greedy**

---

# 🏆 Most Important Patterns for You

If your goal is to become strong in **Python + Data Engineering**, prioritize these:

| Priority | Pattern               | Problems           |
| -------- | --------------------- | ------------------ |
| ⭐⭐⭐⭐⭐    | Dictionary / Hash Map | 71, 80, 107        |
| ⭐⭐⭐⭐⭐    | Set                   | 74, 84, 106        |
| ⭐⭐⭐⭐⭐    | Two Pointers          | 76, 77, 78, 88, 89 |
| ⭐⭐⭐⭐⭐    | Sliding Window        | 105                |
| ⭐⭐⭐⭐⭐    | Prefix Sum            | 90, 91, 107        |
| ⭐⭐⭐⭐     | Sorting               | 78, 85, 87, 101    |
| ⭐⭐⭐⭐     | Greedy                | 72, 109, 110       |
| ⭐⭐⭐⭐     | Kadane                | 73, 108            |
| ⭐⭐⭐⭐     | Intervals             | 101, 102           |
| ⭐⭐⭐      | Matrix                | 98, 99, 100        |
| ⭐⭐⭐      | Index manipulation    | 82, 95, 97         |

The biggest goal for this level should be that when you see a new array problem, you can look at it and say:

> **"This looks like a Hash Map problem."**

or

> **"This is a Two Pointer problem."**

or

> **"This is a Sliding Window problem."**

That recognition is the real skill you're building.
