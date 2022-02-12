class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        temp = list()
        temp.extend(nums)
        nums.clear()
        
        for x in temp:
            if x not in nums:
                nums += [x]
        
        
        return len(nums)


