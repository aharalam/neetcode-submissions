# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        head = ListNode()
        current_node_for_megalist = head

        current_node_for_list1 = list1
        current_node_for_list2 = list2

        while current_node_for_list1 or current_node_for_list2:
            if current_node_for_list1 == None:
                current_node_for_megalist.val = current_node_for_list2.val
                current_node_for_list2 = current_node_for_list2.next
                if current_node_for_list2:
                    temp = ListNode()
                    current_node_for_megalist.next = temp
                    current_node_for_megalist = temp
                continue
            if current_node_for_list2 == None:
                current_node_for_megalist.val = current_node_for_list1.val
                current_node_for_list1 = current_node_for_list1.next
                if current_node_for_list1:
                    temp = ListNode()
                    current_node_for_megalist.next = temp
                    current_node_for_megalist = temp
                continue
            if current_node_for_list1.val < current_node_for_list2.val:
                current_node_for_megalist.val = current_node_for_list1.val
                current_node_for_list1 = current_node_for_list1.next
            else:
                current_node_for_megalist.val = current_node_for_list2.val
                current_node_for_list2 = current_node_for_list2.next
            if current_node_for_list1 or current_node_for_list2:
                temp = ListNode()
                current_node_for_megalist.next = temp
                current_node_for_megalist = temp
        
        return head
