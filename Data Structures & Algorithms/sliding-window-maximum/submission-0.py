class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for r in range(k-1, len(nums)):
            l = r-k+1
            res.append(max(nums[l:r+1]))
        return res