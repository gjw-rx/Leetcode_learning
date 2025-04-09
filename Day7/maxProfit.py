from typing import List
class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        minValue = 1000000
        maxProfit = -1
        for i in range(len(prices)):
            if(prices[i]<minValue):
                minValue = prices[i]
            elif(prices[i]-minValue>maxProfit):
                maxProfit = prices[i]-minValue
        return maxProfit