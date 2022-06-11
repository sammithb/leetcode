# Order (n) time and Order (1) space solution 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_count = 0
        
        for i in range(0, len(nums)):
            if nums[i] == val:
                # checking if the value given is one of the indices in the list nuns 
                num_count += 1
                #if you see it increase the final count given, or as shown in the description "K", increase that by 1
                
            else :
                #case for if the value is not in the index num
                nums[i-num_count] = nums[i]
                #assign the remaining numbers in the array to nums[i], if the val is not already equal to it
                
        return len(nums) - num_count