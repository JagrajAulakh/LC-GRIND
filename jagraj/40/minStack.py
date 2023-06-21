class MinStack:

    def __init__(self):
        self.minElement = float("inf")
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minElement = val
            return

        if val > self.minElement:
            self.stack.append(val)
            return
        
        self.stack.append(2*val - self.minElement)
        self.minElement = val
        

    def pop(self) -> None:
        if not self.stack:
            return

        self.minElement = self.minElement if self.stack[-1] > self.minElement else 2*self.minElement - self.stack[-1]
        del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1] if self.stack[-1] > self.minElement else self.minElement

    def getMin(self) -> int:
        return self.minElement
        


