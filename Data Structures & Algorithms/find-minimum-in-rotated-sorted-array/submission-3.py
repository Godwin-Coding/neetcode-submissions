class Solution:
    def findMin(self, nums: list[int]) -> int:
        start, end = 0, len(nums)-1

        while end-start > 1:

            mid = (start+end)//2

            if nums[mid] > nums[start] and nums[mid] > nums[end]:
                start = mid
            
            elif (nums[mid] < nums[start] and nums[mid] < nums[end]) or nums[mid] > nums[start] and nums[mid] < nums[end]:
                end = mid

        return min(nums[start], nums[end])
        