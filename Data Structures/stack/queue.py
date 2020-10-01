class Stack:
    def __init__(self):
        super().__init__()
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def isEmpty(self):
        return len(self.stack) == 0
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
class Queue:
    def __init__(self):
        super().__init__()
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self, data):
        while len(self.stack1) != 0:
            self.stack2.push(self.stack1.pop())
        
        self.stack1.push(data)

        while len(self.stack2) != 0:
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        if not self.stack1.isEmpty():
            return self.stack1.pop()

class Queue2:
    def __init__(self): 
        self.s = [] 
          
    # Enqueue an item to the queue  
    def enQueue(self, data): 
        self.s.append(data) 

    def deQueue(self):
        if len(self.s) <= 0:
            return

        x = self.s[len(self.s) - 1]
        self.s.pop()

        if len(self.s) <= 0:
            return x

        item = self.deQueue()
        self.s.append(x)
        return item