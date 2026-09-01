class ContainsDuplicate:
    
    # brute foce method:
    def containsDuplicate(self, nums:list[int])-> bool:
        for i in range(len(nums)):
            for j in range( i+1, len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
    # sort first
    def containsDuplicate2(self, nums:list[int]) -> bool:
        nums.sort()
        for i in range (1,len(nums)):
            if nums[i]== nums[i-1]:
                return True
        return False
    
    # Set or hash set
    def containsDuplicate3(self, nums:list[int])-> bool:
        hashSet:set[int]=set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False
    
    
    
    
    # test code 
obj = ContainsDuplicate()
nums =[1,2,3,1]
print(obj.containsDuplicate3(nums))