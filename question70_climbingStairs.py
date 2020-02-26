class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        stair=list()
        stair.append(1)
        stair.append(1)
        for i in range (2,n+1):
            stair.append(stair[i-2]+stair[i-1])
        return stair[n]