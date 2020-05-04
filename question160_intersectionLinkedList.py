# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        counter = dict()
        c = headA
        while c is not None:
            counter[c] =1
            c = c.next
        
        c = headB
        while c is not None:
            if c not in counter:
                c = c.next
                continue
            return c
        return None