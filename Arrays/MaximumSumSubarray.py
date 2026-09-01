"""
Kadane's Algorithm
==================

Problem:
--------
Find the maximum sum of a contiguous subarray.

Example:
--------
Input:
    [5, 2, -5, -6, 9, 7, 2, -1, 7]

Maximum contiguous subarray:
    [9, 7, 2, -1, 7]

Maximum sum:
    24


1. What is a Contiguous Subarray?
---------------------------------

A contiguous subarray is a continuous section of an array.

Rules:
    - Elements must be next to each other.
    - No elements can be skipped.
    - The original order must be maintained.

Example:
    Array = [1, 2, 3, 4, 5]

Valid contiguous subarrays:
    [1]
    [1, 2]
    [1, 2, 3]
    [2, 3]
    [2, 3, 4]
    [3, 4, 5]

Invalid:
    [1, 3]
    [2, 4]
    [1, 3, 5]

Why invalid?
    Because elements have been skipped.


2. Number of Contiguous Subarrays
---------------------------------

For an array containing n elements:

    Number of contiguous subarrays = n * (n + 1) / 2

Example:

    n = 4

    Number of subarrays:
        4 * 5 / 2
        = 10

The reason is:

    Starting from index 0:
        4 possibilities

    Starting from index 1:
        3 possibilities

    Starting from index 2:
        2 possibilities

    Starting from index 3:
        1 possibility

    Total:
        4 + 3 + 2 + 1 = 10


3. Maximum Subarray Problem
---------------------------

The problem asks:

    "Among all possible contiguous subarrays,
     which one has the largest sum?"

Example:

    [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Maximum subarray:

    [4, -1, 2, 1]

Sum:

    4 + (-1) + 2 + 1 = 6

Answer:

    6


4. Brute Force Approach
-----------------------

The simplest idea is:

    1. Generate every possible contiguous subarray.
    2. Calculate the sum of every subarray.
    3. Keep track of the largest sum.
    4. Return the largest sum.

For n elements, there are:

    n * (n + 1) / 2

possible contiguous subarrays.

Therefore, the number of subarrays grows approximately as:

    O(n^2)


5. Improved Brute Force
-----------------------

Instead of calculating the sum of every subarray from
the beginning, maintain a running sum.

Example:

    [4, -1, 2, 1]

Starting from 4:

    [4]
        sum = 4

    [4, -1]
        sum = 3

    [4, -1, 2]
        sum = 5

    [4, -1, 2, 1]
        sum = 6

This avoids recalculating the entire subarray sum.

Time complexity:

    O(n^2)

Space complexity:

    O(1)


6. Kadane's Algorithm
---------------------

Kadane's Algorithm improves the problem from O(n^2)
to O(n).

The key idea is:

    At every element, decide:

        1. Should I start a new subarray here?
        OR
        2. Should I continue the previous subarray?

These are the only two meaningful choices.


7. The Two Variables
--------------------

Kadane's Algorithm mainly maintains two values:

    current:
        The maximum sum of a contiguous subarray
        ending at the current position.

    best:
        The maximum sum found anywhere in the array
        so far.

Think of them as:

    current = "What is the best sum ending HERE?"

    best = "What is the best sum I have seen ANYWHERE?"


8. The Main Decision
--------------------

Suppose the current element is X.

There are two possibilities.

Option 1:
    Start a new subarray with X.

    Sum = X

Option 2:
    Continue the previous subarray.

    Sum = current + X

Choose whichever is larger.

Mathematically:

    new_current = max(X, current + X)


9. Why Are There Only Two Choices?
----------------------------------

Suppose we are at element X.

Any contiguous subarray ending at X must be one
of these:

    [X]

OR:

    [previous contiguous subarray, X]

We cannot skip elements because the subarray must
be contiguous.

Therefore, there are only two possibilities:

    Start fresh
    Continue previous


10. Why Do We Discard a Negative Current Sum?
----------------------------------------------

Suppose:

    current = -4

and the next element is:

    X = 9

Two choices:

    Start fresh:
        9

    Continue:
        -4 + 9 = 5

Starting fresh is better:

    9 > 5

Therefore, the negative running sum is discarded.

Mathematically, if:

    current < 0

then for any future value X:

    current + X < X

Therefore, carrying a negative sum forward can
never improve a future subarray.

This is the mathematical reason behind the
"reset" behavior in Kadane's Algorithm.


11. Important: Negative Number vs Negative Sum
----------------------------------------------

Do NOT think:

    "If the current number is negative,
     immediately reset."

That is incorrect.

Example:

    [10, -9, 10]

The number -9 is negative.

But:

    10 + (-9) = 1

The running sum is still positive.

Continuing gives:

    1 + 10 = 11

Starting fresh at the final 10 gives:

    10

Therefore:

    11 > 10

So we should NOT reset because an individual
number is negative.

The correct rule is:

    If the accumulated current sum becomes negative,
    discard the accumulated sum.


12. Example
-----------

Consider:

    [5, 2, -5, -6, 9, 7, 2, -1, 7]


Step 1:
    Start with 5.

    current = 5
    best = 5


Step 2:
    Add 2.

    Continue:
        5 + 2 = 7

    Start fresh:
        2

    Choose 7.

    current = 7
    best = 7


Step 3:
    Add -5.

    Continue:
        7 - 5 = 2

    Start fresh:
        -5

    Choose 2.

    current = 2
    best = 7

    Notice:
        The current sum decreased,
        but it is still positive.

    Therefore, keep it.


Step 4:
    Add -6.

    Continue:
        2 - 6 = -4

    Start fresh:
        -6

    Choose -4.

    current = -4
    best = 7

    current is now negative.

    Therefore, this accumulated group is
    no longer useful for future elements.


Step 5:
    Add 9.

    Continue:
        -4 + 9 = 5

    Start fresh:
        9

    Choose 9.

    current = 9
    best = 9

    This is where we effectively start a new
    subarray.


Step 6:
    Add 7.

    Continue:
        9 + 7 = 16

    Start fresh:
        7

    Choose 16.

    current = 16
    best = 16


Step 7:
    Add 2.

    Continue:
        16 + 2 = 18

    Start fresh:
        2

    Choose 18.

    current = 18
    best = 18


Step 8:
    Add -1.

    Continue:
        18 - 1 = 17

    Start fresh:
        -1

    Choose 17.

    current = 17
    best = 18

    The current sum decreased from 18 to 17,
    but it is still positive.

    Therefore, keep it.


Step 9:
    Add 7.

    Continue:
        17 + 7 = 24

    Start fresh:
        7

    Choose 24.

    current = 24
    best = 24


13. Complete Example Table
--------------------------

    Element     Current       Best
    -------     -------       ----
       5            5           5
       2            7           7
      -5            2           7
      -6           -4           7
       9            9           9
       7           16          16
       2           18          18
      -1           17          18
       7           24          24

Final:

    best = 24


14. Maximum Subarray
--------------------

The maximum subarray is:

    [9, 7, 2, -1, 7]

Its sum is:

    9 + 7 + 2 - 1 + 7
    = 24

Therefore:

    Maximum sum = 24


15. The Important Transition
----------------------------

The most important part of the example is:

    5 → 7 → 2 → -4

At -4:

    current < 0

Therefore:

    Discard the previous accumulated group.

Then:

    9 → 16 → 18 → 17 → 24

This becomes the new useful group.


16. Kadane's Mathematical Formula
---------------------------------

Let:

    A[i] = current array element

    current[i] =
        maximum sum of a contiguous subarray
        ending at position i

Then:

    current[i] =
        max(
            A[i],
            current[i - 1] + A[i]
        )

In simple words:

    current =
        maximum(
            start fresh,
            continue previous
        )


17. Global Maximum
-------------------

The current value tells us the best sum ending
at the current position.

But the final answer could have occurred earlier.

Therefore, maintain:

    best =
        maximum(best, current)

In simple words:

    current = best sum ending HERE

    best = best sum found ANYWHERE SO FAR


18. Dynamic Programming Connection
----------------------------------

Kadane's Algorithm is a Dynamic Programming technique.

Why?

Because the current answer depends on the previous
answer.

We calculate:

    current[i]

using:

    current[i - 1]

This is called a state transition.

State:

    current[i]

Transition:

    current[i] =
        max(A[i], current[i - 1] + A[i])


19. Why Kadane Uses O(1) Space
------------------------------

A normal Dynamic Programming solution might store:

    current[0]
    current[1]
    current[2]
    ...
    current[n]

That requires O(n) space.

However, current[i] only needs current[i - 1].

Therefore, we only need to remember:

    previous current
    current
    best

The previous states do not need to be stored.

Therefore:

    Space = O(1)


20. Time Complexity
-------------------

Each element is processed exactly once.

For every element, we perform a constant amount
of work:

    - Calculate the continue option.
    - Calculate the start option.
    - Choose the larger value.
    - Update best.

Therefore:

    Time = O(n)

Space:

    O(1)


21. Kadane's Algorithm in Plain-English Pseudocode
--------------------------------------------------

START

    Take the first element.

    Set CURRENT to the first element.

    Set BEST to the first element.

    For every remaining element:

        Ask:
            "Should I start a new subarray here?"

        Calculate:
            current element

        Ask:
            "Should I continue the previous subarray?"

        Calculate:
            CURRENT + current element

        Choose the larger value.

        Store that value as CURRENT.

        Compare CURRENT with BEST.

        If CURRENT is larger:
            update BEST.

    Return BEST.

END


22. The Simple Mental Model
---------------------------

Imagine CURRENT as a group of numbers
that you are carrying.

If the group's sum is positive:

    The group can potentially help
    future elements.

    KEEP IT.


If the group's sum becomes negative:

    The group is hurting future elements.

    THROW IT AWAY.

    Start fresh from the next element.

At the same time:

    BEST remembers the largest sum
    you have ever seen.


23. Example as a Mental Picture
--------------------------------

    5 → 7 → 2 → -4

    Positive → Positive → Positive → Negative

                                      ↓

                                  DROP GROUP

                                      ↓

                         9 → 16 → 18 → 17 → 24

                                      ↓

                                  BEST = 24


24. Important Rules to Remember
--------------------------------

Rule 1:
    Contiguous means no skipping.

Rule 2:
    current = best sum ending at current position.

Rule 3:
    best = largest sum seen anywhere.

Rule 4:
    At every element choose:

        Start fresh
        OR
        Continue previous

Rule 5:
    Negative running sum is harmful.

Rule 6:
    A negative ELEMENT does not automatically
    mean we should reset.

Rule 7:
    A positive running sum can still be useful
    even if the next element is negative.

Rule 8:
    Kadane processes the array only once.

Rule 9:
    Time complexity = O(n).

Rule 10:
    Extra space = O(1).


25. How to Recognize Kadane's Algorithm
---------------------------------------

When a problem contains:

    "maximum sum"

    AND

    "contiguous subarray"

    OR:

    "maximum sum of consecutive elements"

Think:

    KADANE'S ALGORITHM


26. Final Mental Model
----------------------

Do not memorize the code.

Remember this question:

    "Should I continue my current group,
     or should I start a new group here?"

If continuing gives a larger sum:

    CONTINUE

If starting fresh gives a larger sum:

    START FRESH

Then always remember:

    "What is the largest sum I have seen so far?"

That value is the final answer.


27. Core Formula
----------------

The entire Kadane algorithm can be summarized by:

    CURRENT =
        max(
            current element,
            CURRENT + current element
        )

and:

    BEST =
        max(
            BEST,
            CURRENT
        )


Final Result for the Example:
-----------------------------

Input:

    [5, 2, -5, -6, 9, 7, 2, -1, 7]

Maximum contiguous subarray:

    [9, 7, 2, -1, 7]

Maximum sum:

    24

Time Complexity:

    O(n)

Space Complexity:

    O(1)
"""
class MaximumSubarray:
    
    # caluculate sum of array
    def __sumOfarray(self,arr:list[int], start:int,end:int)-> int:
        sum= 0
        for i in range(start,end+1):
            sum= sum+ arr[i]
        return sum

    # brute force method
    # time O(n^3), space O(n)
    def maxSubarrayBrute(self, nums:list[int])-> int:
        
        best= nums[0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                sum=self.__sumOfarray(nums,i,j)
                if sum>best:
                    best=sum
        return best    
    # Kadane algorithm
    def maxSubarrayKaden(self, nums:list[int])-> int:
        current=nums[0]
        best= nums[0]
        for i in range(1, len(nums)):
            current =max(nums[i],current+nums[i])
            if current > best:
                best= current
            
                
        return best
    
    # best way
    def maxSubArryBest(self, nums: list[int])-> int:
        current =nums[0]
        best= nums[0]
        for i in range (1,len(nums)):
            current = current + nums[i]
            if current>best:
                best =current
            if current<0:
                current = 0
        
            
    
obj= MaximumSubarray()
nums=[5, 2, -5, -6, 9, 7, 2, -1, 7]
print(obj.maxSubArryBest(nums=nums))


