# Part of the assignment is to create a program to add and remove
# data, so I wanted to make a test program using an array
# to get an idea of how this would be done.
class List:
  def __init__(self):
    # Internal Array
    self.internalArray = []

  def push(self, item):
    # Add an item onto the list
    self.internalArray.append(item)

  def remove(self, name, age):
    # Return the string "Nothing" if the internalArray is empty,
    # else remove the entry the user wishes to
    if (len(self.internalArray) == 0):
      return "The list is empty, there's nothing to remove"

    # Go through each entry in the list, if it matches the name
    # and age remove and return it, otherwise return false
    for data in self.internalArray:
      if ((data[0] == name) and (data[1] == age)):
        self.internalArray.remove(data)
        return data
    return False
  
  def __str__(self):
    return self.internalArray.__str__()

class Program:
  def __init__(self):
    # Create the list and its
    # functions and call the choosing function
    self.array = List()
    self.choose()

  def choose(self):
    # Keep users in an infinite choice loop until they want to
    # end the program
    choosing = True

    while (choosing == True):
      choice = int(input("What do you wish to do? \n1: Add \n2: Remove \n3: View the list \n4: Quit\n"))
      if (choice == 1):
        self.add()
      elif (choice == 2):
        self.remove()
      elif (choice == 3):
        self.view()
      elif (choice == 4):
        choosing = False
      else:
        print("Not an option")

  def add(self):
    # Ask for a name and age and append this to the array
    name = input("Please enter the name: ")
    age = int(input("Please enter the age: "))
    self.array.push((name, age))
    print(self.array)

  def remove(self):
    # Ask for a name and age which will be searched for through the
    # list class remove function
    name = input("Enter the name of the person you wish to remove: ")
    age = int(input("Enter the age of the person you wish to remove: "))
    removed = self.array.remove(name, age)

    # If it returns false it means the name and age can't be found
    if (removed == False):
      print("Couldn't find the entry")

    # Otherwise, the person was removed, meaning we can print the
    # returned value
    else:
      print("{} was removed.".format(removed))

  def view(self):
    # Simply prints the list to see what's stored inside it
    print(self.array)

# Run the program
Program()