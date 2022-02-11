class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = list()
        open_chars = ['(', '{', '[']
        combo = ['()', '{}', '[]']
        
        s_list = list(s)
        
        while(s_list):
            cur_char = s_list.pop(0)
            if not stack:
                if cur_char not in open_chars:
                    return False
                stack += [cur_char]
            else:
                if cur_char in open_chars:
                    stack += [cur_char]
                else:
                    open_in_stack = stack.pop()
                    
                    if f'{open_in_stack}{cur_char}' not in combo:
                        return False
                    
        if stack:
            return False
        else:
            return True


