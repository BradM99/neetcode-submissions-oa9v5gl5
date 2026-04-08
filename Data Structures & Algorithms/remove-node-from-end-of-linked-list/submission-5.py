# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0

        while current:
            if count == n:
                nthNode = current
            current = current.next
            count += 1
        
        if count == n:
            return head.next
        
        prev = head
        current = head.next

        while nthNode.next:
            prev = current
            current = current.next
            nthNode = nthNode.next
        
        prev.next = current.next

        return head


        
