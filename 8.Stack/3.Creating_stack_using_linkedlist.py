class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        nodeValue = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        node_value = self.LinkedList.head.value
        return node_value
    
    def delete(self):
        self.LinkedList.head = None

stack1 = Stack()
# print(stack1.isEmpty())
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
print(stack1)
print(stack1.pop())
print(stack1.peek())
