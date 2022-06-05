#o(n) time and o(n) space(in place) solution

non_zeroes_index = -1 
        
    for i in range(0, len(nums)):
        if nums[i] != 0: 
            non_zeroes_index += 1 
            nums[non_zeroes_index] = nums[i]
       
    for i in range(non_zeroes_index+1, len(nums)): 
        nums[i] = 0 


#o(n) time and o(n) space(not in place) solution 

result = []
        
    for i in range (0, len(nums)): 
        if nums[i] != 0: 
            result.append(nums[i])
    for i in range (0, len(nums)): 
        if nums[i] == 0: 
            result.append(nums[i])
        
    for i in range(0, len(nums)): 
        nums[i] = result[i]

        