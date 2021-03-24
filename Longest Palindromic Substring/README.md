# [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

Given a string s, return the longest palindromic substring in s.

 

### Example 1:

    Input: s = "babad"  
    Output: "bab"  
    Note: "aba" is also a valid answer.

### Example 2:

    Input: s = "cbbd"  
    Output: "bb"

### Example 3:

    Input: s = "a"  
    Output: "a"

### Example 4:

      Input: s = "ac"  
      Output: "a"

 

### Constraints:

   1 <= s.length <= 1000  
    s consist of only digits and English letters (lower-case and/or upper-case),

<details>
<summary>Solution approach:</summary>
Iterate over every index, and expand outward with that index as a center. Main function can iterate, and use the helper function to check the longest palindrome centered 
  at specific index.
</details>
