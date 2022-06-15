# if len(jewels) = m and len(stones) = n, time = 0(m + n), space = O(m)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        
        result = 0
        
        for stone in stones: 
            if stone in jewels_set: 
                result += 1 
        return result    

'''
# O(mn) time and O(1) space solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int: 
        result = 0 
        
        for stone in stones: 
            if stone in jewels: 
                result += 1 
        return result 
'''         