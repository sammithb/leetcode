# O(n) time and O(1) space solution 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_price = sys.maxsize
        result = 0 
        
        for i in range (len(prices)): 
            result = max(result, prices[i] - lowest_price)
            lowest_price = min(lowest_price, prices[i])
            
        return result 


'''
# O(n) time and O(n) space solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: 
            return 0
        
        max_to_right = prices[:]
        max_to_right[-1] = 0
        for i in reversed(range(0, len(prices)-1)):
            max_to_right[i] = max(prices[i+1], max_to_right[i+1])
        
        possible_profits = []
        for buy in range (0, len(prices)-1): 
            purchase_price = prices[buy]
            max_sale_price = max_to_right[buy]
            possible_profit = max(0, max_sale_price - purchase_price)
            
            possible_profits.append(possible_profit) 
            
        return max(possible_profits)
'''