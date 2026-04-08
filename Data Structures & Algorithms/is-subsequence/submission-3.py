class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        left = 0
        right = 0

        while right < len(t):
            if s[left] == t[right]:
                left += 1
            
            if left == len(s):
                return True
                
            right += 1
        return False
