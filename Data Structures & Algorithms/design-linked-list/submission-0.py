class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0) # dummy head
        self.tail = ListNode(0) # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        # Base case: Check if the index is out of bounds. If it is, return -1:
        if index >= self.size:
            return -1
        
        curr = self.head.next # start at the first real node
        for _ in range(index):
            curr = curr.next
        return curr.val


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        # Point new node to current first real node
        new_node.next = self.head.next

        # Point new node back to dummy head
        new_node.prev = self.head

        # Point current first real node's prev to new node
        self.head.next.prev = new_node

        # Point dummy head's next to new node
        self.head.next = new_node

        # Don't forget to increase the size of the LinkedList by 1
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        # Point new node backward to current last real node
        new_node.prev = self.tail.prev

        # Point new node forward to dummy tail
        new_node.next = self.tail

        # Point current last real node's next to new node
        self.tail.prev.next = new_node

        # Point tail's prev to new node
        self.tail.prev = new_node

        # Don't forget to increase the LinkedList's size by 1
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        # Find the node that will come BEFORE the new node
        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next
        
        # Now insert between prev_node and prev_node.next
        new_node = ListNode(val)
        next_node = prev_node.next

        new_node.next = next_node
        new_node.prev = prev_node
        next_node.prev = new_node
        prev_node.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        for _ in range(index):
            if index >= self.size:
                return
        
        # Find the node BEFORE the one we want to delete
        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next
        
        # The node to delete is the one after prev_node
        node_to_delete = prev_node.next

        #Splice it out by connecting prev_node directly to node_to_delete.next
        prev_node.next = node_to_delete.next
        node_to_delete.next.prev = prev_node

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)