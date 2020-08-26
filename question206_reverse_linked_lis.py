# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # iterative approach
        # prev = None
        # curr = head
        # while curr is not None:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev
        
        
        # Recurrsive
        # Assume list is already reversed
        if head == None or head.next == None:   
                    return head
        
        # 1->2->3->4->5->NULL
        # if we reached to here, it means last node is returned to the previous caller
        # 5 return to 4, 4 return to 3, 3 return to 2 etc...
        
        return_Node = self.reverseList(head.next)  
        head.next.next = head    # i.e. head is currently at 4, 4.next = 5, and we want 
                                 # 5 pointing to 4 (reverse), so that's why head.next.next = head
        head.next = None         # although 5 is now pointing at 4, but 4 is still pointing at 5
                                 # so we set head.next(4.next) to None to get rid of the pointer
        
        return return_Node       # since our return_Node is the last node that we returned, which 
                                 # is pointing at 5. When we reached this line of code.
                                 # it means all the above recursion stacks are runned, so we can 
                                 # return the reversed linked list starting from node 5