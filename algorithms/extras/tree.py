import collections

class TreeNode:
  def __init__(self, value):
    self.left = None
    self.value = value
    self.right = None

  def insert(self, new_value):
    if (new_value < self.value):
      if (self.left != None):
        self.left.insert(new_value)
      else:
        self.left = TreeNode(new_value)
    
    elif (new_value > self.value):
      if (self.right != None):
        self.right.insert(new_value)
      else:
        self.right = TreeNode(new_value)

    else:
      print("{} is already in the tree.".format(new_value))

  def __str__(self):
    return self.value.__str__()

class BinaryTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    if (self.root != None):
      self.root.insert(value)
    else:
      self.root = TreeNode(value)

  def printTree(self, currentNode=None):
    if (currentNode == None):
      currentNode = self.root
    
    if (currentNode.left != None):
      self.printTree(currentNode.left)
    print(currentNode)
    if (node.right != None):
      self.printTree(currentNode.right)

  def bfs(self, to_search):
    queue = collections.deque([])
    queue.append(self.root)
    
    while (len(queue) != 0):
      current_node = queue.popleft()

      if (current_node.value == to_search):
        print("Found {}!".format(to_search))
        return True

      else:
        if (current_node.left != None):
          queue.append(current_node.left)
        if (current_node.right != None):
          queue.append(current_node.right)
    
    print("Couldn't find {}.".format(to_search))
    return False

  def dfs(self, to_search, currentNode=None):
    if (currentNode == None):
      currentNode = self.root
    
    if (to_search == currentNode.value):
      print("Found {}!".format(currentNode.value))
      return True

    elif (to_search < currentNode.value):
      if (currentNode.left != None):
        self.dfs(to_search, currentNode.left)
      else:
        print("Couldn't find {}.".format(to_search))
        return False
    
    elif (to_search > currentNode.value):
      if(currentNode.right != None):
        self.dfs(to_search, currentNode.right)
      else:
        print("Couldn't find {}.".format(to_search))
        return False

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(20)
tree.insert(40)
tree.bfs(20)
tree.dfs(25)