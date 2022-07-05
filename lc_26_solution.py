# O(n) time and O(1) space solution 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        final_element = nums[0]
        k = 1 
            
        for i in range (0, len(nums)):
            if nums[i] != final_element: 
                nums[k] = nums[i]
            
                k += 1 
            
                final_element = nums[i]
        
        return k 

# O(n) time and O(n) space solution

'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        not_repeated_nums = [nums[0]]
        
        for i in range (1, len(nums)): 
            if nums[i] != nums[i-1]: 
                not_repeated_nums.append(nums[i])
            
        for i in range (0, len(not_repeated_nums)): 
            nums[i] = not_repeated_nums[i]
            
        return len(not_repeated_nums)
'''