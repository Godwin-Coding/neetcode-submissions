class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            print(prices[i])
            buy = min(buy, prices[i])
            sell = max(sell, prices[i] - buy)
        return sell

        