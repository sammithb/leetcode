# O(n) time and O(1) space solution 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        
        while index >= 0 and s[index] == " ": 
            index -= 1
        
        end_index = index 
        
        while index >= 0 and s[index] != " ":
            index -= 1
            
        return end_index-index
        
'''
# O(n) time and O(n) space
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        
        words = s.split(" ")
        
        return len(words[-1])
'''