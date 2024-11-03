import Queue_for_level_order as queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBST = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("tea")
coffee = TreeNode("coffee")
rightChild = TreeNode("Cold")
cola = TreeNode("cola")
fanta = TreeNode("fanta")
newBST.leftChild = leftChild
newBST.rightChild = rightChild
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild.leftChild = cola
rightChild.rightChild = fanta

def level_order(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def search_BST(rootNode, nodeValue):
    if not rootNode:
        return "Binary Tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not Found"
    
print(search_BST(newBST, "tea"))