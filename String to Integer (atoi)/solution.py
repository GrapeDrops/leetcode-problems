class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        s = s.strip()
        ans = 0
        sign = 1
        
        if not s:
            return 0
        
        start_idx = 0
        if s[start_idx] == '-':
            start_idx += 1
            sign *= -1
        elif s[start_idx] == '+':
            start_idx += 1
            
        for char in s[start_idx:]:
            if not char.isdigit():
                break
            ans = (ans * 10) + int(char)
        
        return min(max(INT_MIN, ans*sign), INT_MAX)
