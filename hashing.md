Yes. **111–140 is the Hashing / Dictionary / Set level**, and this is a very important step after the array problems you completed.

The main goal here is to recognize:

* **Set** → "Have I seen this?"
* **Dictionary** → "What information do I know about this?"
* **Frequency dictionary** → "How many times?"
* **Index dictionary** → "Where did I see it?"
* **Sliding window + dictionary** → "What is inside my current window?"
* **Grouping dictionary** → "Which items belong together?"

I'll explain each problem, the methods from **worst → best**, Python tools to consider, and real-world scenarios.

---

# Level 3 — Hashing & Dictionaries

## 111. Two Sum using HashMap

### Problem

Given:

`[2, 7, 11, 15]`

target = `9`

Find two numbers that add to 9.

### Basic approach

Nested loops:

**O(n²)**

### Better approach

Use a dictionary:

**value → index**

For each number, calculate:

**target - current**

Then check whether that number has already appeared.

### Complexity

**O(n)** average time
**O(n)** space

### Python

Use:

* `dict`
* `enumerate()`
* `get()` or membership checking

### Scenario

Finding two transactions that combine to a particular amount.

Example:

> Which two payments together equal ₹10,000?

---

# 112. Valid Anagram

### Problem

Determine whether two strings contain exactly the same characters with the same frequencies.

Example:

`listen`

`silent`

They are anagrams.

### Basic approach

Sort both strings.

**O(n log n)**

### Better

Character frequency.

**O(n)**

### Python

Use:

* dictionary
* `collections.Counter`

### Pattern

**Frequency Mapping**

### Scenario

* Search systems
* Word games
* Text normalization
* Detecting rearranged identifiers

---

# 113. Happy Number

### Problem

Repeatedly replace a number with the sum of the squares of its digits.

Eventually:

* If it reaches `1` → happy
* If it enters a cycle → not happy

### Important concept

You need to detect whether you've already seen a number.

### Method

Use a **set of previously seen values**.

### Complexity

Depends on number size, but practically very efficient.

### Python

**Set**

### Pattern

**Cycle Detection using Set**

### Scenario

This teaches a general technique useful when processing:

* state transitions
* repeated calculations
* workflow states
* dependency cycles

---

# 114. Isomorphic Strings

### Problem

Determine whether two strings have the same structural pattern.

Example:

`egg`

`add`

Mapping:

`e → a`

`g → d`

So they are isomorphic.

But:

`foo`

`bar`

is not.

### Important

Mapping must be **one-to-one**.

You can't have:

`e → a`

and later:

`e → b`

### Method

Maintain mappings between characters.

Usually:

**dictionary A → B**

and

**dictionary B → A**

### Complexity

**O(n)**

### Pattern

**Bidirectional Mapping**

### Scenario

Useful conceptually for:

* schema mapping
* field transformations
* symbolic substitution
* data transformation validation

---

# 115. Word Pattern

### Problem

Given a pattern:

`abba`

and words:

`dog cat cat dog`

Determine whether they follow the same pattern.

Mapping:

`a → dog`

`b → cat`

### Important

Like isomorphic strings, mapping must be one-to-one.

### Method

Dictionary mapping.

### Complexity

**O(n)**

### Python

`dict`

### Pattern

**One-to-One Mapping**

### Scenario

Matching:

* templates
* configuration patterns
* data schemas
* event types to categories

---

# 116. Contains Duplicate II

### Problem

Find whether the same value occurs within distance `k`.

Example:

`[1,2,3,1]`

k = `3`

The two `1`s are within distance 3.

### Brute force

Compare nearby pairs.

Potentially:

**O(nk)**

### Better

Store:

**value → latest index**

When you see the same value again:

Calculate:

**current index − previous index**

### Complexity

**O(n)** average

### Pattern

**Hash Map + Index Tracking**

### Scenario

Detecting repeated events within a time window.

For example:

> Did the same user perform the same action twice within 5 minutes?

---

# 117. Longest Consecutive Sequence

You already saw this in #106.

### Problem

`[100,4,200,1,3,2]`

Longest sequence:

`1,2,3,4`

Length:

`4`

### Sorting approach

**O(n log n)**

### Set approach

**O(n)** average

### Pattern

**Set + Sequence Detection**

### Scenario

Finding:

* longest active-day streak
* consecutive IDs
* continuous event sequences
* uptime streaks

---

# 118. Top K Frequent Elements

### Problem

Find the `k` most frequently occurring elements.

Example:

`[1,1,1,2,2,3]`

k = `2`

Answer:

`[1,2]`

### Method 1

Frequency dictionary + sorting.

**O(n log n)**

### Better

Frequency dictionary + heap.

**O(n log k)**

### Another important approach

Bucket sort can achieve:

**O(n)** in suitable conditions.

### Python

Learn:

* `dict`
* `Counter`
* `heapq`

### Pattern

**Frequency + Top K**

### Scenario

Very common:

* Most frequent API errors
* Top-selling products
* Most active users
* Most common log messages
* Most visited URLs

---

# 119. Group Anagrams

### Problem

Group words containing the same characters.

Input:

`["eat","tea","tan","ate","nat","bat"]`

Output groups conceptually:

```text id="m2i3t4"
[eat, tea, ate]
[tan, nat]
[bat]
```

### Basic method

Sort every word and use sorted characters as the key.

For example:

`eat → aet`

`tea → aet`

`ate → aet`

Therefore they belong together.

### Complexity

Approximately:

**O(n × k log k)**

where `k` is word length.

### Better

Character frequency as the key.

Potentially:

**O(n × k)**

### Python

`dict`

`defaultdict(list)`

`Counter`

### Pattern

**Grouping + Frequency Signature**

### Scenario

Grouping:

* equivalent strings
* normalized names
* duplicate records
* data with same characteristics

---

# 120. Find Duplicate Number

### Problem

An array contains numbers where one number is duplicated.

Example:

`[1,3,4,2,2]`

Duplicate:

`2`

### Set method

Track seen values.

**O(n)** space.

### Advanced method

Floyd's Cycle Detection.

**O(n)** time
**O(1)** space

### Pattern

**Cycle Detection**

This is a more advanced problem.

### Scenario

Detecting duplicated IDs when memory usage must be minimal.

---

# 121. Longest Substring Without Repeating Characters

### Problem

Find the longest substring containing no repeated characters.

Example:

`abcabcbb`

Answer:

`abc`

Length:

`3`

### Brute force

Generate every substring.

**O(n²)** or worse.

### Better

**Sliding Window + Set**

### More precise approach

Use:

**Dictionary character → latest index**

### Complexity

**O(n)**

### Python

`set` or `dict`

### Pattern

⭐⭐⭐⭐⭐

**Sliding Window + Hash Map**

### Scenario

Finding the longest sequence of unique:

* events
* user actions
* characters
* IDs

within a stream.

---

# 122. Minimum Window Substring

### Problem

Given:

`string = ADOBECODEBANC`

target:

`ABC`

Find the smallest substring containing A, B, and C.

Answer:

`BANC`

### Brute force

Check all substrings.

Very expensive.

### Better

**Sliding Window + Frequency Dictionary**

Maintain:

* required character counts
* current window counts
* number of required characters satisfied

### Complexity

**O(n)**

### Python

`dict` / `Counter`

### Pattern

⭐⭐⭐⭐⭐

**Variable Sliding Window + Frequency**

### Scenario

Very useful conceptually for:

* finding minimum period containing required events
* log analysis
* time-window queries
* stream processing

---

# 123. Ransom Note

### Problem

Determine whether one string can be constructed from the characters of another string.

Example:

Magazine:

`aab`

Ransom:

`aba`

Possible.

But:

Magazine:

`ab`

Ransom:

`aab`

Not possible.

### Method

Count character frequencies.

### Complexity

**O(n)**

### Python

`Counter`

### Pattern

**Frequency Comparison**

### Scenario

Checking whether available resources are sufficient for a requirement.

For example:

> Do we have enough units of each required component?

---

# 124. Jewels and Stones

### Problem

Given:

Jewels:

`aA`

Stones:

`aAAbbbb`

Count how many stones are jewels.

Answer:

`3`

### Method

Put jewels into a set.

Then scan stones and check membership.

### Complexity

**O(n)** average

### Python

`set`

### Pattern

**Set Membership**

### Scenario

Filtering data based on an allowed category list.

Example:

> Which events belong to the allowed event types?

---

# 125. Find Common Characters

### Problem

Find characters appearing in **every word**, including frequency.

Example:

`["bella","label","roller"]`

Common:

`["e","l","l"]`

Notice `l` appears twice in every word.

### Method

Find frequency for each word and keep the minimum frequency across all words.

### Pattern

**Frequency + Intersection**

### Python

`Counter`

### Scenario

Finding common attributes across multiple datasets.

---

# 126. Unique Number of Occurrences

### Problem

Determine whether every distinct number has a different frequency.

Example:

`[1,2,2,1,1,3]`

Frequencies:

```text id="zj4qhd"
1 → 3
2 → 2
3 → 1
```

All frequencies:

`3,2,1`

They are unique.

### Method

1. Count frequencies
2. Put the counts into a set
3. Compare number of frequencies with number of unique frequencies

### Pattern

**Dictionary + Set**

### Scenario

Validating whether categories have unique occurrence patterns.

---

# 127. Check if Array Pairs Are Divisible by K

### Problem

Can the array be divided into pairs where each pair's sum is divisible by `k`?

Example:

`[1,2,3,4,5,10,6,7,8,9]`

k = `5`

Numbers need matching remainders.

### Key idea

If:

`a % k = r`

then you need another number with remainder:

`k-r`

### Special case

Remainder `0` must pair with remainder `0`.

Remainder `k/2` for even `k` has a special rule.

### Method

**Frequency of remainders**

### Complexity

**O(n)**

### Pattern

**Hash Map + Modulo**

### Scenario

Scheduling or grouping values where combined totals must satisfy a divisibility rule.

---

# 128. Longest Harmonious Subsequence

### Problem

A harmonious subsequence has maximum value − minimum value exactly `1`.

Example:

`[1,3,2,2,5,2,3,7]`

Longest harmonious subsequence:

`[3,2,2,2,3]`

Length:

`5`

### Method

Count frequencies.

For each value `x`, check:

**frequency(x) + frequency(x+1)**

### Complexity

**O(n)** average

### Pattern

**Frequency + Neighbor Lookup**

### Scenario

Finding adjacent category ranges or consecutive metric groups.

---

# 129. Count Nice Pairs

### Problem

This problem is based on a transformation involving a number and its reversed digits.

The key insight is to transform each number into a value such as:

**number − reverse(number)**

Then numbers with the same transformed value form valid pairs.

### Method

Dictionary frequency.

### Complexity

**O(n)** average

### Pattern

**Transform → Group → Count**

### Scenario

This is a good general technique for grouping records according to a derived property.

---

# 130. Continuous Subarray Sum

### Problem

Determine whether there is a continuous subarray whose sum is a multiple of `k`.

### Key concept

Use **prefix sum remainders**.

If two prefix sums have the same remainder when divided by `k`, their difference is divisible by `k`.

### Method

Dictionary:

**remainder → earliest index**

### Complexity

**O(n)**

### Pattern

⭐⭐⭐⭐⭐

**Prefix Sum + Hash Map + Modulo**

### Scenario

Finding continuous periods where a metric satisfies a divisibility condition.

---

# 131. Equal Row and Column Pairs

### Problem

Given a square matrix, count how many rows are exactly equal to columns.

### Example

Conceptually:

Row:

`[1,2,3]`

Column:

`[1,2,3]`

That's a match.

### Efficient method

Convert each row into a hashable representation and count frequencies.

Then compare each column against the row-frequency dictionary.

### Pattern

**Matrix + Hash Map**

### Complexity

Approximately:

**O(n²)** for an `n × n` matrix.

### Scenario

Comparing structured records:

* row schemas
* configuration structures
* repeated matrix patterns

---

# 132. Frequency Sort

### Problem

Sort characters according to frequency.

Example:

`tree`

Frequencies:

`t → 1`

`r → 1`

`e → 2`

Possible result:

`eetr`

### Methods

Frequency dictionary + sorting:

**O(n log n)**

Frequency + buckets can improve performance.

### Python

`Counter`

`sorted()`

### Pattern

**Frequency + Sorting**

### Scenario

Ranking data based on occurrence:

* most common error first
* most common event first
* most used character/token

---

# 133. Intersection of Multiple Arrays

### Problem

Given multiple arrays, find values that appear in **every array**.

Example:

```text id="m9q0q2"
[1,2,3]
[2,3,4]
[2,3,5]
```

Common:

`[2,3]`

### Method

Frequency/count how many arrays contain each number.

Important:

You should count each number **once per array**, not once per occurrence.

### Pattern

**Set Intersection / Frequency Across Collections**

### Scenario

Finding:

* users present in every dataset
* products available in every warehouse
* features common across all files

---

# 134. Find Players With Zero or One Losses

### Problem

Given match results, identify players who have:

* zero losses
* exactly one loss

### Method

Dictionary:

**player → loss count**

Then classify based on count.

### Complexity

**O(n)**

### Pattern

**Frequency Counting**

### Scenario

Exactly the same pattern applies to:

* employees with zero errors
* servers with one failure
* customers with zero complaints
* users with one violation

---

# 135. Number of Good Pairs

### Problem

Count pairs `(i,j)` where:

**i < j**

and:

`nums[i] == nums[j]`

Example:

`[1,2,3,1,1,3]`

There are multiple pairs involving repeated values.

### Brute force

Compare every pair.

**O(n²)**

### Hash Map

When you see a value that has appeared `c` times, it creates `c` new pairs with the current value.

### Complexity

**O(n)**

### Pattern

**Frequency + Combinatorial Counting**

### Scenario

Counting:

* matching users
* duplicate events
* same-category pairs
* matching transaction types

---

# 136. Check if Sentence is Pangram

### Problem

Determine whether a sentence contains every English alphabet letter.

### Method

Put characters into a set.

Then check whether there are all 26 letters.

### Complexity

**O(n)**

### Python

`set`

### Pattern

**Set + Membership**

### Scenario

Checking whether a dataset contains every required category/code/type.

---

# 137. Maximum Number of Balloons

### Problem

Given a string, determine how many times you can construct the word:

`balloon`

### Key idea

Count each character.

Then determine which required character becomes the limiting factor.

Remember:

`l` and `o` are needed twice.

### Method

`Counter` / dictionary

### Complexity

**O(n)**

### Pattern

**Frequency + Minimum**

### Scenario

Resource allocation:

> How many complete products can we manufacture from available components?

---

# 138. Find Lucky Integer

### Problem

Find an integer whose value equals its frequency.

Example:

`[2,2,3,4,4,4]`

Frequencies:

`2 → 2`

`3 → 1`

`4 → 3`

Lucky integers:

`2`

Return the largest lucky integer:

`2`

### Method

Frequency dictionary.

Then find values where:

**value == frequency**

### Complexity

**O(n)**

### Pattern

**Frequency + Filtering + Maximum**

### Scenario

Finding categories whose occurrence matches a required threshold.

---

# 139. Sort Characters by Frequency

This is closely related to #132.

### Problem

Given:

`"tree"`

sort characters from highest frequency to lowest.

Frequency:

`e → 2`

`t → 1`

`r → 1`

Result can be:

`eetr`

### Methods

Frequency + sorting:

**O(n log n)**

Bucket approach:

**O(n)**

### Python

`Counter`

`sorted()`

### Pattern

**Frequency + Sorting**

### Scenario

Ranking:

* log messages
* event types
* tokens
* product categories

by frequency.

---

# 140. Find Difference of Two Arrays

### Problem

Given:

A:

`[1,2,3]`

B:

`[2,4,6]`

Find:

Elements in A but not B:

`[1,3]`

Elements in B but not A:

`[4,6]`

### Method

Convert both to sets.

Then perform set difference.

### Complexity

**O(n+m)** average

### Python

`set`

### Pattern

**Set Difference**

### Scenario

Very useful in Data Engineering.

For example:

Dataset A contains user IDs from yesterday.

Dataset B contains user IDs from today.

You can find:

**A − B**

→ users who disappeared.

**B − A**

→ new users.

---

# 🧠 The Big Patterns in 111–140

This is the most important part.

You don't need to memorize 30 individual solutions.

You need to identify these patterns.

| Pattern                   | Problems                                                   |
| ------------------------- | ---------------------------------------------------------- |
| **Frequency Dictionary**  | 112, 118, 119, 123, 125, 126, 128, 132, 134, 137, 138, 139 |
| **Set Membership**        | 113, 117, 124, 136                                         |
| **Index Tracking**        | 111, 116                                                   |
| **Two-Way Mapping**       | 114, 115                                                   |
| **Sliding Window**        | 121, 122                                                   |
| **Prefix Sum + Hash Map** | 130                                                        |
| **Modulo + Hash Map**     | 127, 130                                                   |
| **Top K**                 | 118                                                        |
| **Grouping**              | 119, 129                                                   |
| **Matrix + Hashing**      | 131                                                        |
| **Set Intersection**      | 125, 133                                                   |
| **Set Difference**        | 140                                                        |
| **Frequency + Sorting**   | 132, 139                                                   |
| **Frequency + Min/Max**   | 137, 138                                                   |
| **Cycle Detection**       | 113, 120                                                   |

---

# ⭐ Python Tools You Should Master

For these problems, concentrate on these Python tools.

## 1. `dict`

Most important.

Use it for:

**value → count**

**value → index**

**character → frequency**

**player → losses**

**remainder → index**

---

## 2. `set`

Use it when your question is:

> "Have I seen this?"

or:

> "Is this value present?"

or:

> "Give me only unique values."

---

## 3. `Counter`

From Python's `collections` module.

This is essentially a specialized dictionary for frequency counting.

Very useful for:

* 112
* 118
* 119
* 123
* 125
* 128
* 132
* 134
* 137
* 138
* 139

But don't just use `Counter` blindly. **Understand how a normal dictionary performs frequency counting first.**

---

## 4. `defaultdict`

Especially useful for:

**Grouping**

For example:

`anagram_signature → list of words`

This is particularly useful for #119.

---

## 5. `heapq`

Useful for:

**Top K**

Especially #118.

It lets you avoid sorting everything when you only need the top `K`.

---

# 🔥 Worst → Best Algorithm Thinking

For this entire level, use this process.

### Step 1 — Brute force

Ask:

> "Can I compare every pair/every substring?"

Usually:

**O(n²)**

---

### Step 2 — Sorting

Ask:

> "Would sorting make relationships easier?"

Usually:

**O(n log n)**

Useful for:

* anagrams
* frequency ranking
* consecutive values

---

### Step 3 — Set

Ask:

> "Do I only need to know whether something exists?"

Use:

**Set**

Examples:

* duplicate detection
* membership
* unique values

---

### Step 4 — Dictionary

Ask:

> "Do I need to remember something about each value?"

Use:

**Dictionary**

Examples:

`number → index`

`character → count`

`player → losses`

---

### Step 5 — Sliding Window

If the problem says:

* substring
* subarray
* continuous
* longest
* shortest
* window

think:

**Sliding Window**

Examples:

**121, 122**

---

### Step 6 — Prefix Sum + Dictionary

If the problem involves:

* subarray sum
* continuous sum
* target sum
* modulo of sums

think:

**Prefix Sum + Hash Map**

Examples:

**107, 130**

---

# 🌍 Real-World Scenarios

These problems become much easier to remember if you connect them to Data Engineering.

### Frequency

`error_type → count`

Used for:

* log analysis
* monitoring
* reporting

---

### Set

`unique_user_ids`

Used for:

* distinct users
* duplicate detection
* data validation

---

### Dictionary lookup

`user_id → user_details`

Used for:

* joins
* lookups
* caching

---

### Index tracking

`event_id → latest_position`

Used for:

* duplicate event detection
* stream processing
* event windows

---

### Grouping

`department → employees`

Used for:

* aggregation
* partitioning
* reporting

---

### Top K

`API endpoint → request count`

Find the top 10.

Used for:

* monitoring
* dashboards
* analytics
* anomaly detection

---

### Sliding Window

`timestamp → event`

Find events in the last 5 minutes.

Used for:

* real-time monitoring
* rate limiting
* fraud detection
* stream processing

---

### Prefix Sum

Find a continuous period where total sales = target.

Used for:

* financial analysis
* resource utilization
* time-series processing

---

# 🎯 What You Should Learn First

For your Python/Data Engineering path, I would prioritize these:

### Level A — Must Know

**111 → Two Sum with Dictionary**

**112 → Frequency**

**116 → Index Tracking**

**117 → Set**

**121 → Sliding Window**

**123 → Frequency**

**124 → Set Membership**

**134 → Frequency**

**135 → Frequency + Counting**

**140 → Set Difference**

---

### Level B — Very Important

**118 → Top K**

**119 → Grouping**

**125 → Frequency Intersection**

**127 → Modulo + Frequency**

**130 → Prefix Sum + Hash Map**

**131 → Hashing 2D data**

---

### Level C — Advanced

**120 → Cycle Detection**

**122 → Minimum Window**

**129 → Transform + Group**

---

# 🧠 The Main Mental Model

When you get a new problem, ask:

> **Do I need to know if I've seen something?**

→ `set`

> **Do I need to count something?**

→ `dict` / `Counter`

> **Do I need to remember where I saw it?**

→ `dict[value] = index`

> **Do I need to map one thing to another?**

→ `dict`

> **Do I need to group things?**

→ `dict` / `defaultdict`

> **Do I need the most frequent K items?**

→ `Counter` + heap/sorting

> **Do I need a longest/shortest substring?**

→ Sliding Window

> **Do I need a continuous subarray with a particular sum?**

→ Prefix Sum + Dictionary

> **Do I need unique/common/different values?**

→ Set

If you become comfortable with these **8–10 patterns**, you'll find that problems 111–140 stop looking like 30 different problems—they become variations of a small number of Python techniques.
