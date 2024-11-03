class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    
    def Enqueue(self,value):
        self.items.append(value)
        return "Item inserted successfully"
    
    def Dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.items[0]
    
    def delete(self):
        self.items = None
        return "All items are deleted"
    
queue1 = Queue()
print(queue1.Enqueue(1))
print(queue1.Enqueue(2))
print(queue1.Enqueue(3))
print(queue1)
print(queue1.Dequeue())
print(queue1)
print(queue1.peek())