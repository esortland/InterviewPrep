# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode('head', None)
        res = head
        while l1 and l2:
            if l1.val < l2.val:
                res.next = ListNode(l1.val, None)
                l1= l1.next
            else:
                res.next = ListNode(l2.val, None)
                l2 = l2.next
            res = res.next
        
        res.next = l1 or l2
            
        return head.next
