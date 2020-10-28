class TreeNode:
  def __init__(self, value):
    self.left = None
    self.value = value
    self.right = None

  def insert(self, newValue):
    if (newValue < self.value):
      # The value is smaller
      if (self.left == None):
        self.left = TreeNode(newValue)
      else:
        self.left.insert(newValue)

    else:
      # The value is larger
      if (self.right == None):
        self.right = TreeNode(newValue)
      else:
        self.right.insert(newValue)
  
  def __str__(self):
    return self.value.__str__()

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, newValue):
    if (self.root != None):
      self.root.insert(newValue)
    else:
      self.root = TreeNode(newValue)

  def printTree(self, currentNode=None):
    if (currentNode == None):
      currentNode = self.root

    if (currentNode.left != None):
      self.printTree(currentNode.left)
      
    print(currentNode)

    if (currentNode.right != None):
      self.printTree(currentNode.right)

tree1 = BinaryTree()
tree1.insert(29)
tree1.insert(20)
tree1.insert(17)
tree1.insert(40)
tree1.insert(25)
tree1.insert(18)
tree1.insert(1)

tree1.printTree()