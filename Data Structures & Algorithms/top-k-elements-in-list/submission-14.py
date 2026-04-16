class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, ans, set_num, most = 0, [], set(nums), nums[0]
        while count < k:
            count += 1
            for v in set_num:
                if nums.count(v) > nums.count(most):
                    most = v
            ans.append(most)
            set_num.remove(most) 
            nums = [e for e in nums if e != most]
        return ans
    