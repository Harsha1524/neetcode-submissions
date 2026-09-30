class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n= len(nums)
        l=0
        nums = sorted(nums)
        for i in range(n-1):
                if nums[i]==nums[i+1]:
                    l=1
                    break
        if l==0:
            return False
        if l==1:
            return True
                    

        