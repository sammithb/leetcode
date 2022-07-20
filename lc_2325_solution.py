# O(n) time and O(1) space solution 

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        mapping = {}
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        a_index = 0 
        k_index = 0
        while a_index < 26:
            if key[k_index] in mapping or key[k_index] == " ":
                k_index += 1 
            else: 
                mapping[key[k_index]] = alpha[a_index]
                k_index += 1 
                a_index += 1 
        
        result = []
        for m in message: 
            if m == " ": 
                result.append(m)
            else: 
                result.append(mapping[m])
        
        return "".join(result)