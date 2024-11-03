class Stack:
    def __init__(self,maxSize):
        self.list = []
        self.maxSize = maxSize
        
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    #isfull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # push
    def push(self, value):
        if self.isFull():
            return "Stack is full"
        self.list.append(value)
        return "Data inserted successfully"

customStack = Stack(2)
customStack.push(1)
customStack.push(2)
print(customStack)
print(customStack.push(3))
