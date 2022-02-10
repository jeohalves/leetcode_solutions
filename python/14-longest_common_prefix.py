class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lowest_size = 999
        
        for cur_str in strs:
            cur_size = len(cur_str)
            if cur_size < lowest_size:
                lowest_size = cur_size
            
        first_str = strs.pop(0)
        prefix = list()
        
        for i in range(lowest_size):            
            for cur_str in strs:
                if cur_str[i] != first_str[i]:                    
                    prefix = ''.join(prefix)                    
                    return prefix
            
            prefix.append(first_str[i])
        
        prefix = ''.join(prefix)                    
        return prefix

