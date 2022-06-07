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


# O(n^2) time and space solution 

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)): 
            for j in range(i+1, len(nums)): 
                sum = nums[i] + nums[j]
                if sum == target: 
                    return [i,j]

'''
                
                