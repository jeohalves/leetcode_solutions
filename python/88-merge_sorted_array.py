class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0        
        nums1_copy = nums1[:m]
        
        while i < len(nums1):
            if nums1_copy and (not nums2 or nums1_copy[0] < nums2[0]):
                nums1[i] = nums1_copy.pop(0)
            elif nums2 and (not nums1_copy or nums1_copy[0] >= nums2[0]):
                nums1[i] = nums2.pop(0)
            i += 1


