class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        counts = {}
        
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        uniquechars = {k:v for k, v in counts.items() if v == 1}
        
        if len(uniquechars) > 0:
            first_char = next(iter(uniquechars.keys()))
            return s.index(first_char)
        
        return -1