class Solution:
    def palindromeFinder(self, s, index):
        secondPalindrome = ""
        leftIndex = index
        rightIndex = index
        while leftIndex >= 0 and rightIndex < len(s) and s[leftIndex] == s[rightIndex]:
            leftIndex -= 1
            rightIndex += 1
        firstPalindrome = s[leftIndex+1:rightIndex]
            
        leftIndex = index
        rightIndex = index + 1
        while leftIndex >= 0 and rightIndex < len(s) and s[leftIndex] == s[rightIndex]:
            leftIndex -= 1
            rightIndex += 1
            secondPalindrome = s[leftIndex+1:rightIndex]
                
        return firstPalindrome if len(firstPalindrome) > len(secondPalindrome) else secondPalindrome
    
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        ans = ""
        
        for index in range(len(s)):
            palindrome = self.palindromeFinder(s, index)
            if len(palindrome) > len(ans):
                ans = palindrome
                
        return ans
