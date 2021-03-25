class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        original_total = sum(range(1,len(nums)+1))
        curr_total = 0
        counts = [0]*len(nums)
        ans = [0,0]
        for n in nums:
            curr_total += n
            counts[n-1] += 1
            if counts[n-1] == 2:
                ans[0] = n
        ans[1] = original_total - curr_total + ans[0]
        return ans
