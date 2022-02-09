class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        i = 0
        
        arr_copy = arr.copy()
        arr.clear()
        
        while i < len(arr_copy):            
            if arr_copy[i] == 0:
                arr += [arr_copy[i]]
                if len(arr) == len(arr_copy):
                    break
                
            arr += [arr_copy[i]]
            i += 1
            if len(arr) == len(arr_copy):
                    break
