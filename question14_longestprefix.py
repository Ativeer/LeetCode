class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre=""        
        if len(strs)==0:
            return pre
        index=0
        for key,val in enumerate(strs[0]):
            for i in range(1,len(strs)):
                if index>=len(strs[i]) or val!=strs[i][key]:
                    return pre
            pre+=val
            index+=1
        
        return pre