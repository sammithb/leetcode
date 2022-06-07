# O(n) time and O(n) space solution 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        reverse_num = num[::-1]
        
        if reverse_num == num: 
            return True 
        else: 
            return False 
        