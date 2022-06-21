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

'''
# O(n log n) time and O(1) space solution 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        majority_number = -1 
        num_count = 0 
        
        L = 0 
        R = 0 
        
        while L < len(nums):
            while R < len(nums) and nums[L] == nums[R]: 
                R += 1 
                
            if R - L > num_count: 
                num_count = R - L 
                majority_number = nums[L]
                
            L = R 
                
        return majority_number 
'''