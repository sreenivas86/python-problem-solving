
class TwoSum:
    '''
    
    '''
    
    # HashMap mehtod
    # Time complexity O(n), space O(n)
    def twoSumHashMap(self, nums: list[int], target: int) -> list[int]:
        seen:list[int]=list()
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen.index(complement), i]

            seen.append(num)

        return []
    # brute force method
    # Time O(n) and space O(1)

    def twoSumBrfm(self, nums: list[int], target: int) -> list[int]:
        for i,num in enumerate(nums):
            for j in range (i,len(nums)):
                complement=num+nums[j]
                if complement== target:
                    return [i,j]
        return []

    # Two pointer method
    # Time O(log n)
    def twoSumTwoPointer(self, nums: list[int], target: int) -> list[int]:
        duplicate=nums
        nums.sort()
        left=0
        right=len(nums)-1
        while left<right:
            a=nums[left]
            b=nums[right]
            complement=a+b
            if target==complement:
                return [duplicate.index(a),duplicate.index(b)]
            elif complement> target:
                right -=1
            else:
                left +=1
        return[]
        

nums = [2, 7, 11, 15]
target = 18

obj = TwoSum()

print(obj.twoSumTwoPointer(nums, target))