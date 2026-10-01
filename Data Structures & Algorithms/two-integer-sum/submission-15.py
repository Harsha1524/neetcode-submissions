class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]== target:
        #             return [i,j]


        # temp =0
        # for i in range(len(nums)):
        #     temp = target - nums[i]
        #     if temp in nums:
        #         for j in range(len(nums)):
        #             if nums[j]==temp and i!=j:
        #                 return [i,j]
        #             else:
        #                 continue
        #     else:
        #         continue


        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i
        return
            