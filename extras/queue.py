class Queue:
  def __init__(self, size):
    self.internalArray = [None] * size # Creates the internal Array
    self.front = 0 # Variable for the front of the queue
    self.back = 0 # Variable for the back of the queue
    self.capacity = 0 # Variable to track the size of the queue

  def add(self, data):
    if (self.capacity == len(self.internalArray)):
      # Error message if the capacity becomes equal to the length of the array
      print("Queue is full.")
      return False
    
    else:
      # Loop to the front of the array if the back is at the end of the array and
      # add the data to the pos of self.back
      if (self.back == len(self.internalArray)):
        self.back = 0

      self.internalArray[self.back] = data
      self.capacity += 1
      self.back += 1
      print("Added {} to the queue.".format(data))

  def remove(self):
    # If the front is equal to none, it means there are no items in the queue, return error
    if (self.internalArray[self.front] == None):
      print("Nothing to remove.")
      return False

    else:
      # Loop to the front of the array if the front reaches the end and remove whatever
      # item is at the pos of self.front
      if (self.front == len(self.internalArray)):
        self.front = 0

      temp = self.internalArray[self.front]
      self.internalArray[self.front] = None
      self.capacity -= 1
      self.front += 1
      print("Removed {} from the queue".format(temp))

  def __str__(self):
    # Returns the contents of internalArray
    return self.internalArray.__str__()

# Testing queue code
queue1 = Queue(5)
print(queue1) # This will print the queue, it will at first be full of None
queue1.remove() # There's nothing to remove, an error is shown

for count in range(5): # Add a range of numbers to the queue
  queue1.add(count)
print(queue1) # The full queue is shown

queue1.add(6) # We attempt to add 6 to the queue, but it's full, error is shown

queue1.remove() # So, we remove whatever's at the front...
print(queue1) # And see that the front is now an empty space...
queue1.add(6) # Meaning the next number can fit in!

print(queue1)