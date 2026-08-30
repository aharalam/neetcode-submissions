class MinStack:

    def __init__(self):
        self.stack = [] # stores actual values
        self.minStack = [] # stores the minimum at each point

    def push(self, val: int) -> None:
        self.stack.append(val)

        # The new minimum is the smaller of (val, current minimum)
        if self.minStack: # if the minStack is not empty
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() # keeps them in sync!

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
