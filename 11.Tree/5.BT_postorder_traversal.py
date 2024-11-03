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

def post_order(rootNode):
    if not rootNode:
        return
    post_order(rootNode.leftChild)
    post_order(rootNode.rightChild)
    print(rootNode.data)

post_order(newBST)