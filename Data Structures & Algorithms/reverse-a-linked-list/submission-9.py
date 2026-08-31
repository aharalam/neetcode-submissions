# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head
        #temp_node = current_node.next # You would need to check if current_node is None in order to do it this way with temp_node as a global variable.

        while current_node:
            temp_node = current_node.next

            current_node.next = previous_node
            previous_node = current_node
            current_node = temp_node
        
        return previous_node


            