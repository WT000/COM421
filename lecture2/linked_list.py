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
    n = Node(data)
    if self.first == None:
      self.first = n # The linked list has already been made but is EMPTY, meaning we can say that "if the linked list is empty (which it is)", put the added node first.
    else:
      self.last.link(n) # If there's already an item in the list, link the newly added node to the existing one

    self.last = n # The last node on the list is finally updated to be the newly added node

list1 = LinkedList()

list1.add(1)
list1.add(2)

print(list1)
# The main program, outside the class as it's not indented
#n1 = Node("Red")
#n2 = Node("Blue")

# Checking the data inside each node
#print(n1)
#print(n2)

# Linking the two nodes together
#n1.link(n2)

# Checking the link between the nodes
#print()
#print(n1.prev)
#print(n1.next)
#print(n2.prev)
#print(n2.next)
#print()