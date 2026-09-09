class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxPay = 0
        for sell in prices:
            maxPay = max(maxPay, sell - minBuy)
            minBuy = min(minBuy, sell)
            
        return maxPay