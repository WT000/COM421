class Node:
  def __init__(self, data):
    # Node attributes
    self.prev = None
    self.data = data
    self.next = None

  def link(self, newNode):
    # This is used on the last node when adding a new node, make:
    # self.next on the self.last node equal to the NEW node
    # self.prev on the NEW node equal to the self.last node
    self.next = newNode
    newNode.prev = self

  def __str__(self):
    return self.data.__str__()

class LinkedList:
  def __init__(self):
    # A reference to the first and last node
    self.first = None
    self.last = None

  def add(self, data):
    # Create the node itself
    n = Node(data)

    # If there is currently nothing in self.first it means the
    # list is empty, make this equal to the new node
    if (self.first == None):
      self.first = n
    
    # However, if there's already a node (or nodes) in the list,
    # link the last node to the newly added node and update the
    # reference to the last node
    else:
      self.last.link(n)
    self.last = n

  def get(self, index):
    # Start from the first node and use a while loop to go through
    # the list until we reach the target index, return none if we
    # can't find the node
    count = 0
    current_node = self.first
    
    while (count < index):
      if (current_node.next != None):
        current_node = current_node.next
        count += 1
      else:
        return None
    
    return current_node

# Create the node and test it
linkedlist = LinkedList()

linkedlist.add("Cat")
linkedlist.add("Dog")
print(linkedlist.get(0))
print(linkedlist.get(1))
print(linkedlist.get(2))
print(linkedlist.get(3))