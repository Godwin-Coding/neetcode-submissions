class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for e in nums:
            if nums.count(e) > 1:
                return True
        return False
        