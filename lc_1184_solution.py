# O(n) time and O(1) space solution 
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        d = 0 
        
        st = min(start, destination)
        dest = max(start, destination)
        
        for i in range (st, dest): 
            d += distance[i] 
            
        r_d = sum(distance) - d
        
        return min (d, r_d)            