class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #at any given time, either the left or right half is fully sorted
        # find out which side is sorted w.r.t the mid-point, see if the number fits in the range
        # if it does, check that sorted half in the next iteration
        # if it does not, check the other half which may or may not be sorted in the next iteration
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:  # left half is sorted
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:  # right half is sorted
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1