"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def __init__(self):
        self.visited = {}
        
    def copyRandomList(self, head):
        if head is None:
            return None

        if head in self.visited:
            return self.visited[head]

        new_node = Node(head.val)
        self.visited[head] = new_node

        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)
        
        return new_node