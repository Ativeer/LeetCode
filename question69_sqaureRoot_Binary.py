class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x<2:
            return x
        start=0
        end=int(x/2)+1
        while(start<=end):
            mid=int((start+end)/2)
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                start=mid+1
            else:
                end=mid-1
        if mid*mid>x:
            return mid-1
        return mid