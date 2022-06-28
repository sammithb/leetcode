# O(n) time and O(1) space solution 

class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        while n != 1 and n != -1:
            
            if n % 90 == 0: 
                n = n // 90
            
            elif n % 60 == 0: 
                n = n // 60 
            
            elif n % 30 == 0:
                n = n // 30
                
            elif n % 15 == 0:
                n = n // 15
                
            elif n % 6 == 0:
                n = n // 6
                
            elif n % 5 == 0:
                n = n // 5
                
            elif n % 3 == 0:
                n = n // 3
                
            elif n % 2 == 0:
                n = n // 2
                
            else:
                return False
            
        return True