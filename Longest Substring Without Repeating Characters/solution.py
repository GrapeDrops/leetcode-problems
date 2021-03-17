class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_in_window = set()
        i, j = 0, 0
        ans = 0
        
        while j < len(s):
            if s[j] not in letters_in_window:
                letters_in_window.add(s[j])
                j += 1
            else:
                ans = max(ans, j-i)
                letters_in_window.remove(s[i])
                i += 1
                
        return max(ans, j-i)
