# O(n) time and O(n) space solution

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        num_count = {}
        
        for num in nums: 
            
            if num in num_count: 
                num_count[num] += 1 
                
            else: 
                num_count[num] = 1 
        
        for num in num_count: 
            
            if num_count[num] == 1: 
                return num 
            
'''
# O(n log n) time and O(1) space solution

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        
        left = 0
        
        while left < len(nums): 
            right = left 
            
            while right < len(nums) and nums[left] == nums[right]: 
                right += 1 
            
            if left+1 == right:
                return nums[left]
            else: 
                left = right 
'''