class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def recurse(start, end):
            if start > end:
                return -1
            else:
                mid = (end+start)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return recurse(start, mid-1)
                else:
                    return recurse(mid+1, end)

        return recurse(0, len(nums)-1)
        