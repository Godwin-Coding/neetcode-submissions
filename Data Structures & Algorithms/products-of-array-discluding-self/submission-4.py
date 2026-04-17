class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        ans = list()

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]

        postfix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i] * postfix[i+1]

        ans.append(postfix[1])
        for i in range(1, len(nums)-1):
            ans.append(prefix[i-1] * postfix[i+1])
        ans.append(prefix[-2])
        return ans
        