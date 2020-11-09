class TreeNode:
  def __init__(self, value):
    # Each node has a reference to the left and right node along with its own value
    self.left = None
    self.value = value
    self.right = None

  def insert(self, new_value):
    # If the value is lower, it means we need to put the node on the left. 
    # If there's no value in a nodes self.left, put it there. 
    # Else, go into the left node and repeat the process.
    if (new_value < self.value):
      if (self.left == None):
        self.left = TreeNode(new_value)
      else:
        self.left.insert(new_value)
    
    # If the value is greater, it means we need to put the node on the right. 
    # If there's no value in a nodes self.right, put it there. 
    # Else, go into the right node and repeat the process.
    elif (new_value > self.value):
      if (self.right == None):
        self.right = TreeNode(new_value)
      else:
        self.right.insert(new_value)
    
    # Else, the number is already in the tree, in this case we'll reject it.
    else:
      print("Can't accept duplicates.")
      return False

  def __str__(self):
    return self.value.__str__()

class BinaryTree:
  def __init__(self):
    # The first node will become the root of the tree
    self.root = None

  def insert(self, value):
    # If the root is not equal to none, we go into the root node and call the recursive
    # insert function inside it. If it is equal to none, it means the tree is empty, make the
    # value a TreeNode and reference it as the root.
    if (self.root != None):
      self.root.insert(value)
    else:
      self.root = TreeNode(value)

  def printTree(self, root=None):
    # This part of the method allows us to not give any parameters when we want to print the
    # tree
    if (root == None):
      root = self.root

    # If there's a node in root.left, we recursively call it until we get to a node without a left
    # attribute
    if (root.left != None):
      self.printTree(root.left)

    # Once there, we print the value in the node
    print(root.value)

    # Then, we check if there's a node on the right, if there is we recursively call it
    if (root.right != None):
      self.printTree(root.right)

tree = BinaryTree()
tree.insert(20)
tree.insert(10)
tree.insert(15)
tree.insert(13)

tree.printTree()