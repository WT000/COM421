class Stack:
  def __init__(self):
    self.internalArray = []

  def push(self, item):
    self.internalArray.append(item)

  def pop(self):
    # Add an if statement to see if the stack is empty
    if (len(self.internalArray) == 0):
      print("Stack is empty.")
    else:
      a = self.internalArray[-1] # Define the value first so we don't lose it
      del self.internalArray[-1]
      return a # Classes are like bubbles, so the methods need to return data to the outside world

  def peek(self):
    b = self.internalArray[-1]
    return b

  def __str__(self):
    return self.internalArray.__str__()

# Pushing to the stack
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
print(stack1)

# Lets variable "a" = the return value of pop
pop1 = stack1.pop()
pop2 = stack1.pop()

# Then the main program can print it. 
print(pop1)
print(pop2)
print(stack1)

# Popping more in the Stack
pop3 = stack1.pop()
pop4 = stack1.pop()
print(pop3)
print(pop4)

# Popping an empty Stack, causing an error message
pop5 = stack1.pop()

# Pushing new values onto the stack
stack1.push(5)
stack1.push(6)
print(stack1)

# Peeking
peek1 = stack1.peek()
print(peek1)
print(stack1)