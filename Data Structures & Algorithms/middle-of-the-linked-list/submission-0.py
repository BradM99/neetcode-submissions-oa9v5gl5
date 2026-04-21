# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listlen = 0
        current = head

        while current:
            listlen += 1
            current = current.next
    
        middle = (listlen // 2) + 1
        
        while head:
            middle -= 1
            if middle == 0:
                return head
            head = head.next