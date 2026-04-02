class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = -prices[0]
        sold = 0
        cooldown = 0

        for i in range(1, len(prices)):
            temp_h = max(holding, cooldown- prices[i])
            temp_s = holding + prices[i]
            temp_c = max(cooldown, sold)
            holding = temp_h
            sold = temp_s
            cooldown = temp_c
        return max(sold, cooldown)

        