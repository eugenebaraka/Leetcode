class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        increment = int("".join(str(num) for num in digits)) + 1
        
        return [int(d) for d in str(increment)]
        