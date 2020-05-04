class Solution(object):
    def rot(self,A,ind):
        return(A[ind+1:len(A)]+A[0:ind+1])    
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B:
            return True
        for key,val in enumerate(A):
            C=self.rot(A,key)
            print(A)
            if C==B:
                return True
        return False
