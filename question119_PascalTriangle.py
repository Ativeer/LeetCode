class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        global_list=list()
        global_list.append(1)
        if rowIndex==0:
            return global_list
        for i in range(1,rowIndex+1):
            local_list=list()
            local_list.append(1)
            for j in range(1,i):
                local_list.append(global_list[i-1][j]+global_list[i-1][j-1])
            local_list.append(1)
            global_list.append(local_list)
        return global_list[rowIndex]