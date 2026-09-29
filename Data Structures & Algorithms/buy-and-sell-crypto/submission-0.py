class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        answer=0
        for i in range(1,len(prices)):
            if prices[i]<prices[left]:
                left=i
            else:
                profit=prices[i]-prices[left]
                answer=max(answer,profit)
        return answer