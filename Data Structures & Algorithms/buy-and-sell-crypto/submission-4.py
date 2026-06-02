class Solution:
    def maxProfit(self, prices: List[int]) -> int:   

        cost = 0
        n = len(prices)
        i = 0
        for j in range(n):
            if prices[j] - prices[i] < 0:
                i = j 
            cost = max(cost, prices[j]-prices[i]) 

        return cost

        # cost = 0 
        # n = len(prices)

        # def f(i,j,n): 
        #     nonlocal cost 
        #     if i >= j:
        #         return 

        #     cost = max(cost ,prices[j] - prices[i]) 
        #     f(i+1,j,n) 
        #     f(i,j-1,n) 

        #     return 
        # f(0,n-1,n)

        # return cost
            
        