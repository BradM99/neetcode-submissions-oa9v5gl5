# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = head
        prev = head
        beforeLeft = None
        current = head
        node = 1

        start = head

        if left == right:
            return head
        
        while current:
            if node >= left and node < right:
                if node == left:
                    leftToRight = current
                    beforeLeft = prev

                nextPtr = current.next
                current.next = prev
                prev = current
                current = nextPtr

            elif node == right:
                if left == 1:
                    start = current
                beforeLeft.next = current
                nextPtr = current.next
                current.next = prev
                prev = current
                leftToRight.next = nextPtr
                current = nextPtr
            else:
                prev = current
                current = current.next
            node += 1

        return start