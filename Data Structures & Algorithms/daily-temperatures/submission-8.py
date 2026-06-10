class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            j = -1
            term = -len(stk)
            while stk and temperatures[stk[j]] < temperatures[i]:
                res[stk[j]] = i-stk[j]
                stk.pop()
            stk.append(i)
        return res