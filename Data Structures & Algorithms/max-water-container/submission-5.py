class Solution:
    def maxArea(self, heights):
        res = 0
        right = len(heights)-1
        for i in range(len(heights)-1):
            if i > 0 and heights[i] == heights[i-1]:
                continue
            while right > i:
                if (right-i) * min(heights[i], heights[right]) > res:
                    res = (right-i) * min(heights[i], heights[right])
                right -= 1
            right = len(heights)-1
        return res  