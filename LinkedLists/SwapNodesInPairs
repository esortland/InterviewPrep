# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        guard = p0 = ListNode("DUMMY")
        guard.next = head
        
        while p0.next and p0.next.next:
            p1, p2 = p0.next, p0.next.next
            
            p0.next, p1.next, p2.next = p2, p2.next, p1
            
            p0 = p0.next.next
            
        return guard.next
