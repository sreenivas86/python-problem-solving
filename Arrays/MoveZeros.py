class Movezeros:
    
    # bruteforce O(n2) and O(1)
    def movezeros1(self, nums:list[int])->None:
        n=len(nums)
        for i in range(n):
            for j in range(1,n-i):
                if nums[j-1]==0:
                    nums[j-1],nums[j]=nums[j],nums[j-1]
                    
    
    # Aditional array o(n) and O(n)
    
    def moveszeros2(self,nums:list[int])-> None:
        n=len(nums)
        ans=[0]*n
        flag=0
        for i in nums:
            if i !=0:
                ans[flag]=i
                flag +=1
        nums[:]=ans
    # Two pointers
    def moveszeros3(self, nums:list[int])->None:
        i=0
        for j in range(len(nums)):
            if nums[j] !=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            
            
            
obj=Movezeros()
nums=[0,8,0,1,0,3,12,8]
obj.moveszeros3(nums)
print(nums)
            