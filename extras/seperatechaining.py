class Hash:
  # Creates the internal Array and allows the other methods to
  # see the size of the internal Array
  def __init__(self, size):
    self.internalArray = [None] * size
    self.size = size

  def hashTotal(self, raw_data):
    total = 0
    count = 0

    # Each character (from left to right) is turned into its ASCII
    # value, this value is then multiplied by 31 to the power of 
    # the loop number (x * 31**y --- where x is the character and y
    # is the loop number)
    for character in raw_data:
      calculation = ord(character) * (31**count)
      total += calculation
      count + 1

    # The end number is very large, so we use modulo to lower it
    total %= self.size
    return total

  def put(self, key, value):
    # Run the hash calculation on the key, create an empty list if
    # there isn't any and then append the value
    hash_calc = self.hashTotal(key)
    
    if (self.internalArray[hash_calc] is None):
      self.internalArray[hash_calc] = []
    self.internalArray[hash_calc].append((key, value))

  def get(self, key):
    # Run the hash calc and then look for the value, if we find None
    # then we can immediately say it can't be found, else we go
    # through the list and check if the word exists
    hash_calc = self.hashTotal(key)

    if (self.internalArray[hash_calc] == None):
      print("Not found.")
    
    else:
      for word, value in self.internalArray[hash_calc]:
        if (word == key):
          print(value)
          return
      print("Not found.")     

  def __str__(self):
    return self.internalArray.__str__()

hashtable = Hash(127)
hashtable.put("Ant", "Small insect!")
hashtable.put("Termite", "Rivals of ants!")
hashtable.get("Termite")
hashtable.get("test")

print(hashtable)