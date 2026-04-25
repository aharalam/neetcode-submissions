# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create an array
        elements = []

        # Loop through the linked list using the head. Take each value
        # and put it into the array.
        while head != None:
            elements.append(head.val)
            head = head.next

        # Reverse elements
        elements.reverse()
        print(elements)

        # Create a dummy list node called newNode = ListNode()
        newNode = ListNode()

        # Set the currentNode to the head of the LinkedList (newNode)
        currentNode = newNode # currentNode creates the LinkedList

        for element in elements:
            currentNode.next = ListNode(element)
            currentNode = currentNode.next

        print(newNode.next)
        return newNode.next


        

        