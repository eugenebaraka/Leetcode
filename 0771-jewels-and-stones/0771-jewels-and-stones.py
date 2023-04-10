class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # membership testing in set faster than string searching ()(1)
        jewels_set = set(jewels)
        
        return sum(1 for stone in stones if stone in jewels_set)
        