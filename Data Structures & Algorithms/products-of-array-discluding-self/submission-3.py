class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for i in range(len(nums))]

        ans, total = list(), 1
        for e in nums:
            if e != 0:
                total *= e
        for i in range(len(nums)):
            if 0 not in nums:
                ans.append(int(total / nums[i]))
            elif nums[i] == 0:
                ans.append(total)
            else:
                ans.append(0)

        return ans
        