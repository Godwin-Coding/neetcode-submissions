class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            print("for temp", temperatures[i])
            j = -1
            term = -len(stk)
            while j >= term:
                if stk and temperatures[stk[j]] < temperatures[i]:
                    res[stk[j]] = i-stk[j]
                    print("removed", stk.pop())
                else:
                    break
            stk.append(i)
            print(stk)
        return res