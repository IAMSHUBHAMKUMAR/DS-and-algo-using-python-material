class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    # prepand - adding node in begining
    def prepand(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    # adding node anywhere
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            tem_node = self.head
            for _ in range(index-1):
                tem_node = tem_node.next
            new_node.next = tem_node.next
            tem_node.next = new_node
        self.length+=1
        return True

    # traversing
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    #searching
    def search(self,target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index +=1
        return -1
    
    # get method- to find the elements of given index
    def get(self,target):
        if target < 0 or target > self.length:
            return None
        current = self.head
        for _ in range(target):
            current = current.next
        return current
    
    # set method - given value and target to set the value in given target
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.prepand(1)
new_linked_list.prepand(0)
new_linked_list.insert(0,50)
print(new_linked_list)
# new_linked_list.traverse()
# print(new_linked_list.search(40))
# print(new_linked_list.get(-1))
print(new_linked_list.set(2,99))
print(new_linked_list)