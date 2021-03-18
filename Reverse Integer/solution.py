class Solution:
    def reverse(self, x: int) -> int:
        num_string = str(abs(x))
        sign = 1 if x >= 0 else -1
        reversed_num = int(num_string[::-1]) * sign
        
        return reversed_num if -2**31 <= reversed_num <= 2**31-1 else 0
