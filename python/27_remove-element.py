class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        while val in nums:
            idx = nums.index(val)
            nums.pop(idx)
        
        return len(nums)


