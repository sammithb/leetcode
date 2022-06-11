# Order (n) time and Order (1) space solution 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_count = 0
        
        for i in range(0, len(nums)):
            if nums[i] == val:
                num_count += 1
                
            else :
                nums[i-num_count] = nums[i]
                
        return len(nums) - num_count