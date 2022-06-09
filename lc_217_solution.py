# O(n) time and O(n) space solution 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers_seen = set()
        
        for num in nums: 
            if num in numbers_seen: 
                return True 
            numbers_seen.add(num)
        return False 

'''
O(n log n) time and O(n log n) space solution 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = nums.sort()
        
        for i in range(1, len(nums)):
            
            if nums[i] == nums[i - 1]:
                return True
        return False

'''