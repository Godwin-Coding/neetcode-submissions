class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = dict()
        for n in set(nums):
            track[nums.count(n)] = list()
        for n in set(nums):
            track[nums.count(n)].append(n)
        ans = []
        while len(ans) < k:
            ans.extend(track[max(track)])
            track.pop(max(track))
        return ans
