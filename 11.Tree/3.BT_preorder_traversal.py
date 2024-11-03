class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBST = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBST.leftChild = leftChild
newBST.rightChild = rightChild

def pre_order(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    pre_order(rootNode.leftChild)
    pre_order(rootNode.rightChild)

pre_order(newBST)