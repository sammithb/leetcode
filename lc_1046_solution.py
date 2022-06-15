class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range (0, len(stones)): 
            stones[i] *= -1 
        
        heapq.heapify(stones) 
        
        while len(stones) > 1: 
            l1 = heapq.heappop(stones) * -1
            l2 = heapq.heappop(stones) * -1
         
            diff = abs(l1-l2)
            
            heapq.heappush(stones, -1 * diff)
        
        return -(stones[0])



# sum from i = 2 to i = n, i log i 
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # sorting has to be used here so any n log n sorting will work
        
        while len(stones) > 1:
            
            stones.sort()
            s1 = stones.pop()
            s2 = stones.pop()
            stones.append(abs(s1 - s2))
            # it has to be an absolute value because the appended number cannot be negative 
            
        return stones[0]
'''