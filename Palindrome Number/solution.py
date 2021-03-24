class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse_num = 0
        temp_x = x
        
        while temp_x:
            reverse_num = reverse_num*10 + temp_x%10
            temp_x //= 10
            
        return x == reverse_num
