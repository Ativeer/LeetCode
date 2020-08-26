# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ListNode(0)
        ans = cur
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp = ListNode(l1.val)
                ans.next = temp
                l1 = l1.next
            
            elif l1.val > l2.val:
                temp = ListNode(l2.val)
                ans.next = temp
                l2 = l2.next
            ans = ans.next
            
        while l1 != None:
            temp = ListNode(l1.val)
            ans.next = temp
            l1 = l1.next
            ans = ans.next
        
        while l2 != None:
            temp = ListNode(l2.val)
            ans.next = temp
            l2 = l2.next
            ans = ans.next
        
        return cur.next
    