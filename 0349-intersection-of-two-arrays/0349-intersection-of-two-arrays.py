class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        
        if len_nums1 >= len_nums2:
            return [num for num in set(nums2) if num in nums1]
        
        return [num for num in set(nums1) if num in nums2]
        
        