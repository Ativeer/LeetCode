class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # d = dict()
        # for i in nums:
        #     if i in d:
        #         return True
        #     d[i] = 0
        #     d[i] += 1
        # return False
            
        
        return len(nums) > len(set(nums))