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

def in_order(rootNode):
    if not rootNode:
        return
    in_order(rootNode.leftChild)
    print(rootNode.data)
    in_order(rootNode.rightChild)

in_order(newBST)