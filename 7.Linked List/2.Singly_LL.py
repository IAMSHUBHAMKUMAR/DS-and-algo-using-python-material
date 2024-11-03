class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    # created LL with one node having head and tail
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

new_linked_list = LinkedList(10)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.lenght)

# Empy LL
class EmptyLinkedList:

    # created LL with one node having head and tail
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0
