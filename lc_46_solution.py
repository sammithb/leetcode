# O(n ^ n) time and o(n) space solution 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper (nums, partial, used): 
            if len(partial) == len(nums): 
                result.append(partial.copy())
            
            else: 
                for num in nums: 
                    if num not in used: 
                        used.add(num)
                        partial.append(num)
                        
                        helper(nums, partial, used)
                        partial.pop()
                        used.remove(num)
        
        result = []
        partial = []
        used = set()
        helper(nums, partial, used)
        
        return result 