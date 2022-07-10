# O(n) time and O(1) space solution

class Solution:
    def checkRecord(self, s: str) -> bool:
        
        absent_count = 0 
        not_eligible = 'LLL'
        
        for char in s: 
            if char == 'A': 
                absent_count += 1
         
        if absent_count >= 2 or not_eligible in s: 
            return False 
        else: 
            return True 