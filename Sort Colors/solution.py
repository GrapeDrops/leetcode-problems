class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_count = [0]*3
        
        for num in nums:
            nums_count[num] += 1
        
        for i in range(0, nums_count[0]):
            nums[i] = 0
        for j in range(nums_count[0], nums_count[0] + nums_count[1]):
            nums[j] = 1
        for k in range(nums_count[0] + nums_count[1], len(nums)):
            nums[k] = 2
            
        pass
