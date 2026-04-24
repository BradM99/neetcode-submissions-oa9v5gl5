class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxp = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                maxp = max(maxp, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1
            
        return maxp