# O(log n) time and O(1) solution

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        if n % 2 == 1:
            return False
        
        while n != 1:
            n /= 2
            
            if n%2 == 1 and n != 1:
                return False
        
        return True