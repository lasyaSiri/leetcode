class Solution(object):
    def isSubsequence(self, s, t):
        if not s:  
            return True
        s_ptr, t_ptr = 0, 0 
        while t_ptr < len(t):
            if s_ptr < len(s) and s[s_ptr] == t[t_ptr]:  
                s_ptr += 1  
            t_ptr += 1  
            if s_ptr == len(s):  
                return True
        return False