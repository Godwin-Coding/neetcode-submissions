class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            hold = numbers[i]
            for j in range(i+1, len(numbers)):
                if hold + numbers[j] == target:
                    return [i+1, j+1]