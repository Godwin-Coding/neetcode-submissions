class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                res[stk[-1]] = i-stk[-1]
                stk.pop()
            stk.append(i)
        return res