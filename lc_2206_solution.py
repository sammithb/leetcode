# O(n) time and O(n) space solution

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        number_repeats = {}
        
        for i in nums: 
            
            if i in number_repeats: 
                
                number_repeats[i] += 1
                
            else:
                
                number_repeats[i] = 1
                
        num_count = 0 
        
        for keys, values in number_repeats.items(): 
            
            if values % 2 != 0: 
                
                num_count += 1 
        
        if num_count != 0: 
            
            return False 
        
        else: 
            return True 