class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)*(len(nums)+1)/2
        return int(total - sum(nums))
