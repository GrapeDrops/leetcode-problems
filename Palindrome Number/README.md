# [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

### Example 1:

    Input: x = 121
    Output: true

### Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

### Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

### Example 4:

    Input: x = -101
    Output: false

 

### Constraints:

-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

 
Follow up: Could you solve it without converting the integer to a string?

<details>
  <summary>Solution approach</summary>
  Easiest way would be to convert to string and check if it is equal to its reverse. Without string conversion, we could instead build the reverse number by extracting one digit 
  at a time, then comparing to original number
</details>
