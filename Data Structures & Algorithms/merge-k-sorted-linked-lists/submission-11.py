# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        while len(lists) > 1:
            i = 0

            while i + 1 < len(lists):
                dummy = ListNode()
                tail = dummy

                list1 = lists[i]
                list2 = lists[i + 1]

                while list1 and list2:
                    if list1.val < list2.val:
                        tail.next = list1
                        list1 = list1.next
                    else:
                        tail.next = list2
                        list2 = list2.next

                    tail = tail.next

                if list1:
                    tail.next = list1

                if list2:
                    tail.next = list2

                lists[i] = dummy.next
                lists.pop(i + 1)

                i += 1

        return lists[0]