class Node:
  def __init__(self, data):
    # Nodes in a linked list have these three attributes:
    self.data = data
    self.next = None
    self.prev = None

  def link(self, otherNode): # OtherNode is the parameter to this method
    self.next = otherNode # Forward link
    otherNode.prev = self # Backwards link

  def __str__(self): # Defines how we return data associated to this class (the Node's)
    return self.data.__str__()

class LinkedList:
  def __init__(self):
    # A reference to the first node in the list
    self.first = None
    # A reference to the last node, which will be used to add new nodes to the end
    self.last = None

  def add(self, data):
    n = Node(data) # Used to add the node itself
    if (self.first == None): # If there's currently no first node it means the list is empty, make the added node the first node
      self.first = n
    else: # However, if there's currently a node in the linked list, link the existing last node to the new mode
      self.last.link(n)
    self.last = n # Update the reference point, the newest node needs to be the last node

  def get(self, index):
    current_node = self.first # Get the node at the start of the list
    count = 0 # Control variable
<<<<<<< HEAD
    # or while ((count < index) and (current_node is not None)
=======
    
>>>>>>> origin/main
    while ((count < index) and (current_node != None)): # Until the count becomes greater than the index and current_node doesn't hit the end of the list, keep going through each node
          current_node = current_node.next
          count += 1
      
    return current_node # Now that the count is not lower than the users inputted number, the returned node will be the users desired node

list1 = LinkedList()

list1.add(1)
list1.add(2)
list1.add(3)
print(list1.get(0))
print(list1.get(1))
print(list1.get(2))
print(list1.get(100))