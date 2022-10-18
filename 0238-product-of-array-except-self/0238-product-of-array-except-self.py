class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
           prefix=1
           n=len(nums)
           ans=[1]*n
           for i in range(n):
               ans[i]=prefix
               prefix*=nums[i]
           postfix=1
           for i in range(n-1,-1,-1):
                ans[i]*=postfix
                postfix*=nums[i]
           return ans
            