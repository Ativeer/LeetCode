class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        
        i=2
        while (i*i<=x):
            i=i+1
        if i==(x+1):        
            return i
        return i-1