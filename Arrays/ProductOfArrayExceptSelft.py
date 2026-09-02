class ProductOfArrayExceptSelf:
    
    # bruteforce
    def prodOfArrself(self, nums:list[int])-> list[int]:
        n=len(nums)
        ans=[1]*n
        for i in range(n):
            prod=1
            for j in range(n):
                if i==j:
                    continue
                else:
                    prod *=nums[j]
            ans[i]=prod
        return ans
    
    # prefix suffix pattern
    
    def ProdofArrPS(self, nums:list[int])-> list[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        ans=[1]*n
        # caluculate prefix
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        # caluculate suffix
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        # calucualte ans
        for i in range(n):
            ans[i]=suffix[i]*prefix[i]
        
        return ans