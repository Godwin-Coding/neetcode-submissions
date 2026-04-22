class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            if prices[i] == buy:
                continue
            buy, sell = min(buy, prices[i]), max(sell, prices[i] - buy)
        return sell

        