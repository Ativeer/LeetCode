class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new_num=0
        for val,i in enumerate(digits):
            new_num+=i*(10**(len(digits)-val-1))
            print(new_num)
        new_num+=1
        num=[x for x in str(new_num)]
        return num