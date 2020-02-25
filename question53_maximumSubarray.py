class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is []:
            return 0
        a=nums[0]
        msa=nums[0]
        for n in range(1, len(nums)):            
            a=max(nums[n],a+nums[n])
            if a>msa:
                msa=a
        return msa