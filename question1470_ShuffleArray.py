class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pos = 0
        for i in range(0, n-1):
            for x in range(0, n-i-1):
                nums[n+i-x], nums[n-1+i-x] = nums[n+i-x-1], nums[n+i-x]
        return nums