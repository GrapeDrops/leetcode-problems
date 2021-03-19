class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        
        cycle = 2*numRows - 2
        ans = ""
        len_s = len(s)
        
        for row in range(numRows):
            for idx in range(0, len_s, cycle):
                if row+idx >= len_s:
                    break
                ans += s[row+idx]
                if not (row == 0 or row == numRows-1) and (cycle + idx - row < len_s):
                    ans += s[cycle + idx - row]
        
        return ans
        
