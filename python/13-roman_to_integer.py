class Solution:
    def romanToInt(self, s: str) -> int:
        
        number = 0
        
        sbl = dict()
        sbl['I'] = 1
        sbl['V'] = 5
        sbl['X'] = 10
        sbl['L'] = 50
        sbl['C'] = 100
        sbl['D'] = 500
        sbl['M'] = 1000
        
        s_list  = list(s)
        
        while s_list:
            cur = s_list.pop(0)     
            
            if s_list and sbl[cur] < sbl[s_list[0]]:
                next_value = sbl[s_list.pop(0)]
                number += next_value - sbl[cur]
            else:
                number += sbl[cur]
        
        return number


