class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            j = 0
            while j < len(q):
                if temperatures[i] > temperatures[q[j]]:
                    res[q[j]] = i-q[j]
                    q.remove(q[j])
                    j -= 1
                j += 1
            q.append(i)
        return res
        