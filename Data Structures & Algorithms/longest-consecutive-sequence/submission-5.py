class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(sorted(set(nums)))
        new_count, old_count = 1, 1
        for i in range(len(nums)-1):
            if nums[i] - nums[i+1] == -1:
                new_count += 1 
            
            else:
                if new_count > old_count:
                    old_count, new_count = new_count, 1
                else:
                    new_count = 1

        if new_count > old_count:
            return new_count
        return old_count        