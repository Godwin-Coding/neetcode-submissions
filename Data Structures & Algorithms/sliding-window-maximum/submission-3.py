class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        r = 0
        curr_max = -float('inf')
        curr_max_i = None
        while r < k:
            if nums[r] > curr_max:
                curr_max = nums[r]
                curr_max_i = r
            r += 1
        res.append(curr_max)
        l = 1
        while r <= len(nums)-1:
            if l > curr_max_i:
                place_holder = l
                curr_max = -float('inf')
                for i in range(l, r):
                    if nums[i] > curr_max:
                        curr_max = nums[i]
                        curr_max_i = i
                l = place_holder
            if nums[r] > curr_max:
                curr_max = nums[r]
                curr_max_i = r
            res.append(curr_max)
            r += 1
            l += 1
        return res
            
