class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solns = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                sum_val = curr + nums[left] + nums[right]
                if sum_val == 0:
                    solns.add((curr, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum_val < 0:
                    left += 1
                else:
                    right -= 1

        res = [list(x) for x in solns]
        
        return res