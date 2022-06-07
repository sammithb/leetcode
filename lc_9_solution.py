# O(n) time and O(n) space solution 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        reverse_num = num[::-1]
        
        if reverse_num == num: 
            return True 
        else: 
            return False 
    
# O(n) time and O(n) space solution without converting to a string 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x 
        rev_num = 0 
        while num > 0: 
            rev_num = rev_num * 10 + num%10 
            num = num // 10 
        if x == rev_num: 
            return True 
        else: 
            return False 