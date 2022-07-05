# O(log n) time and O(1) space solution

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        #all numbers to the power 2 are positive 
        
        if n == 1:
            return True
        #only to the power 0 is 1, this accounts for that case
        
        if n % 2 == 1:
            return False
        #if it is a power of two it cannot be an odd number 
        
        while n != 1:
            n /= 2
        #assigning a new value for n, calculating if it is to the power two or not 
            
            if n%2 == 1 and n != 1:
                return False
        #checking if there is a remainder and if it is not equal to 1 
            
        if n == 1:
            return True