# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head
        prev = d
        

        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next
        prev2 = None

        for _ in range(right - left + 1):
            temp = curr.next 
            curr.next = prev2
            prev2 = curr
            curr = temp
        
        prev.next.next = curr
        prev.next = prev2 
        return d.next
            

        