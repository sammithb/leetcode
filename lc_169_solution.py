# O(n) time and O(n) space solution 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        num_count = {}
        for num in nums: 
            if num in num_count: 
                num_count[num] += 1
            else: 
                num_count[num] = 1
                
        max_count = 0 
        
        for num in num_count: 
            max_count = max(max_count, num_count[num])
            
        for num in num_count: 
            if num_count[num] == max_count: 
                return num 