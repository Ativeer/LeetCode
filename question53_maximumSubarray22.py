class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        res = [nums[0]]
        s = 0
        for i in range(1, len(nums)):
            s = max(res[i-1] + nums[i], nums[i])
            res.append(s)
        return max(res)