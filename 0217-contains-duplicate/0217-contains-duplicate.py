class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        new_set = set(nums)
        
        return len(new_set) != len(nums)