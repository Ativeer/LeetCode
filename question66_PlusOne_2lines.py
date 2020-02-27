class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x1=int(''.join(str(x) for x in digits))+1
        return list(str(x1))