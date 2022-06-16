# O(n) time and O(1) space solution 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        
        carry = 1 
        for i in range (0, len(digits)): 
            total = digits[i] + carry 
            digits[i] = total % 10
            carry = total // 10 
        if carry != 0: 
            digits.append(carry)
        
        digits.reverse()
        
        return digits 

'''
#O(n) time and O(n) space solution 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0 
        for i in range (0, len(digits)): 
            num = num * 10 + digits[i]
        
        num += 1 
        
        result = []
        
        while num > 0: 
            result.append(num % 10)
            num //= 10 
            
        result.reverse()
        
        return result 
'''