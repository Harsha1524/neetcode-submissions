class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n= len(nums)
        l=0
        for i in range(n):
            for j in range(i):
                if nums[i]==nums[j]:
                    l=1
                    break
        if l==0:
            return False
        if l==1:
            return True
                    

        