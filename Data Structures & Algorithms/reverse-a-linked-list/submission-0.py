# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        res_head = head
        curr = head.next
        res_head.next = None

        while curr.next is not None:
            temp = res_head
            res_head = curr
            curr = curr.next
            res_head.next = temp
        
        curr.next = res_head
        res_head = curr
        
        return res_head
