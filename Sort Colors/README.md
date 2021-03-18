# [Sort Colors](https://leetcode.com/problems/sort-colors/)

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

 

### Example 1:

    Input: nums = [2,0,2,1,1,0]  
    Output: [0,0,1,1,2,2]

### Example 2:

    Input: nums = [2,0,1]  
    Output: [0,1,2]

### Example 3:

    Input: nums = [0]  
    Output: [0]

### Example 4:

    Input: nums = [1]  
    Output: [1]

 

### Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is 0, 1, or 2.

<details>
<summary>Solution approach:</summary>
Make two passes where first pass counts the number of 0s, 1s, and 2s, then second pass substitutes values in order based on the count.  
  Alternative: Keep two pointers, left and right, which indicate next place to put in a 0 or 2, respectively. Then iterate from left to right swapping values accordingly based on 
  the two pointers, and move those pointers towards their next position.
</details>
