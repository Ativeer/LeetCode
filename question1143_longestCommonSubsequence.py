class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        a=len(text1)
        b=len(text2)
        new_matrix=[[None]*(b+1) for i in range(a+1)]
        for i in range(a+1):
            for j in range(b+1):
                if i==0 or j==0:
                    new_matrix[i][j]=0
                elif text1[i-1]==text2[j-1]:
                    new_matrix[i][j]=1+new_matrix[i-1][j-1]
                else:
                    new_matrix[i][j]=max(new_matrix[i-1][j],new_matrix[i][j-1])
        return new_matrix[a][b]
        