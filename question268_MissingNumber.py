class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = len(nums)*((len(nums)+1)/2)
        return int(temp - sum(nums))