class Solution:
    #bad solution 
    def strStr(self, haystack: str, needle: str) -> int:
        
        haystack = list(haystack)
        needle = list(needle)
        idxs = list()
        
        if not needle:
            return 0
        
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                idxs += [i]

        if idxs:
            for idx in idxs:
                if idx+len(needle) <= len(haystack):
                    if haystack[idx:idx+len(needle)] == needle:
                        return idx
            
                
        return -1


