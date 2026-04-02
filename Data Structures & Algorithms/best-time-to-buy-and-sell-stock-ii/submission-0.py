class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = -prices[0]
        sold = 0
        not_holding = 0

        for i in range(1, len(prices)):
            temp_h = max(holding, not_holding - prices[i])
            temp_n = max(not_holding, holding + prices[i])
            holding = temp_h
            not_holding = temp_n
        return not_holding
        