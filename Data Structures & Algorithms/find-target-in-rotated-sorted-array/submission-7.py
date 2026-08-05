class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums)-1

        while end-start > 1:

            mid = (start+end)//2
            #print("start:", start, "mid:", mid, "end:", end, "nums[mid]:", nums[mid])
            if nums[mid] == target:
                return mid  

            if nums[start] <= target <= nums[mid]:
                end = mid-1

            elif nums[mid] <= target <= nums[end]:
                start = mid+1

            elif nums[end] >= target and nums[mid] >= target:
                if nums[start] > nums[mid]:
                    end = mid-1
                else:
                    start = mid+1

            elif nums[start] <= target and nums[mid] <= target:
                if nums[end] < nums[mid]:
                    start = mid+1
                else:
                    end = mid-1

            else:
                break

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1