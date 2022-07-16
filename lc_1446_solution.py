# O(n) time and O(1) space solution

class Solution:
    def maxPower(self, s: str) -> int:
        
        count = 0 
        max_count = 0 
        previous_number = None 
        
        for x in s: 
            if x == previous_number: 
                
                count += 1
                
            else: 
                previous_number = x
                
                count = 1
            
            max_count = max(max_count, count)
        
        return max_count 