# O(n) time and O(1) space solution 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_count = 0
        
        for i in range(0, len(nums)):
            # If number at index i is equal to val, increment the count 
            # of the number of times val has been seen
            if nums[i] == val:
                val_count += 1
            # if the number at index i is not equal to val 
            # copy the number at index i to it's left by skipping the count 
            # of times val has been seen so far
            else :
                nums[i - val_count] = nums[i]
        # return the count of values in the list that are not equal to 
        # val       
        return len(nums) - val_count


        # O(n) time and O(n) space, not in place solution
        '''
        class Solution:
            def removeElement(self, nums: List[int], val: int) -> int:
                temp = []
                for num in nums: 
                    if num != val: 
                    temp.append(num)
                for i in range(0, len(temp)): 
                     nums[i] = temp[i] 
        
                return len(temp)            
        '''