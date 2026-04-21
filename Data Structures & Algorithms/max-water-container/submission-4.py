class Solution:
    def maxArea(self, heights):
        res, done = 0, set()
        right = len(heights)-1
        for i in range(len(heights)-1):
            if heights[i] in done:
                continue
            while right > i:
                if (right-i) * min(heights[i], heights[right]) > res:
                    res = (right-i) * min(heights[i], heights[right])
                right -= 1
            right = len(heights)-1
            done.add(heights[i])
        return res  