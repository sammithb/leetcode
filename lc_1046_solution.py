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