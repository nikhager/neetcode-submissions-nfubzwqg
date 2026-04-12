class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lo = prices[0]
        
        for p in prices:
            if p < lo:
                lo = p
            if (p - lo) > max_profit:
                max_profit = p - lo
        
        return max_profit