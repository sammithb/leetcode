# O(n) time and O(2n) space solution 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key_value_dict = {}
        
        for i in range (0, len(nums)): 
            num = target - nums[i]
            
            if num in key_value_dict: 
                return[key_value_dict[num], i]
            else: 
                key_value_dict[nums[i]] = i 
                
                