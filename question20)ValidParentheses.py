class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        HashTable = {')': '(', ']': '[', '}': '{'}
    	stack = []
    	for char in s:
    		if char in HashTable:
    			if stack:
    				if HashTable[char] == stack.pop():
    					continue
    				else:
    					return False
    			else:
    				return False
    		else:
    			stack.append(char)
        return True if not stack else False