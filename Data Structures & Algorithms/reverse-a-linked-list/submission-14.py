# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list, or single node (already reversed)
        if not head or not head.next:
            return head
        
        new_head = self.reverseList(head.next) # reverse everything after head

        # now head.next points to the new tail of the reversed rest
        head.next.next = head
        head.next = None

        return new_head