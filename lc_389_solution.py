# O(n) time and O(n) space solution

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        letter_count = {}
        
        for letter in t: 
            if letter in letter_count: 
                letter_count[letter] += 1
            else: 
                letter_count[letter] = 1
                
        for letter in s: 
            letter_count[letter] -= 1 
            
            if letter_count[letter] == 0: 
                del letter_count[letter]
            
        for letter in letter_count: 
            return letter