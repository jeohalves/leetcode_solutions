class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        str_x = str(x)        
        for i in range(len(str_x)//2+1):
            if str_x[i] != str_x[-i-1]:
                return False
            
        
        return True

