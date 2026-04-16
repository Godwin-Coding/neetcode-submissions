class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for e in range(len(nums)):
            for i in range(e+1,len(nums)):
                if nums[e] + nums[i] == target:
                    return [e,i]
                
        