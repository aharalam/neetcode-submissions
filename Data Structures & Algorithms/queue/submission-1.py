class Deque:
    
    def __init__(self):
        self.queue = []

    def isEmpty(self) -> bool:
        return not self.queue

    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        self.queue.append(value)
        self.queue.insert(0, self.queue.pop())

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue.pop()
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.queue.pop(0)
