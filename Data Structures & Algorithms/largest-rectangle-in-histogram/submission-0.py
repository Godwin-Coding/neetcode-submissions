class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        def find_width(n):
            ans = 1
            i = 0
            cont = 0
            while i < len(heights):
                if heights[i] >= n:
                    cont += 1
                else:
                    ans = max(ans, cont)
                    cont = 0
                i += 1
            ans = max(ans, cont)
            return ans

        res = 0
        for i in range(1, max(heights)+1):
            res = max(res, find_width(i) * i)
        return res


        