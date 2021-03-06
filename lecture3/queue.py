# Create a queue class which:
# Creates the queue with empty values, set the front and back methods
class Queue:
  def __init__(self, capacity=5):
    self.internalArray = [None] * capacity
    self.capacity = capacity
    self.front = 0 # Index number of the front
    self.back = 0 # Index number of the back
    self.max = 0

# Add needs to add the item to the back of the queue
  def add(self, item):
    if (self.max == self.capacity):
      #print("Can't add {}, the queue is full.".format(item))
      return False # Returning false or true makes the code more reusable
    else:
      self.max += 1
      self.internalArray[self.back] = item # Set the back of the queue to be the item being added
      self.back += 1
      if (self.back == self.capacity):
        self.back = 0
      return True

# Remove needs to delete the item at the front of the queue and shift the queue up one and return what was removed
  def remove(self):
    if self.max == 0:
      return None # indicates that it couldn't be removed, then the main program could print a error message in response
    self.max -= 1
    to_remove = self.internalArray[self.front]
    self.internalArray[self.front] = None # Remove the front of the queue and shift it up
    self.front += 1
    # or if self.front > len(self.internalArray)
    if (self.front == self.capacity):
      self.front = 0
    return to_remove

# Use str to return actual text to the user (in this case, the queue)
  def __str__(self):
    return self.internalArray.__str__()

queue1 = Queue(5)
queue1.add("job1")
queue1.add("job2")
queue1.add("job3")
queue1.add("job4")
queue1.add("job5")
queue1.add("job6")
print(queue1)

queue1.remove()
print(queue1)
queue1.add("job6")
print(queue1)