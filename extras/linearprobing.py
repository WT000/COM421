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
    second_total = total % self.size
    return second_total

  def put(self, key, value):
    # Here I used a different approach to the loop, instead of using
    # a while loop you can instead use a for loop. We loop for the
    # total amount of items in the list, the index we use is
    # calculated by adding the loop number to the hash_calc and
    # using modulo to get the remainder.

    # This means the loop can wrap around itself!
    hash_calc = self.hashTotal(key)

    for count in range(0, self.size):
      index = (hash_calc + count) % self.size
      if (self.internalArray[index] == None):
        self.internalArray[index] = (key, value)
        return

    print("No available space")
    return False

  def get(self, key):
    # Loops through the buckets until it finds the key it's looking
    # for, then prints the associated value
    hash_calc = self.hashTotal(key)

    for count in range(0, self.size):
      index = (count + hash_calc) % self.size
      if (self.internalArray[index][0] == key):
        print(self.internalArray[index][1])
        return

    print("Not found")
    return False   

  def __str__(self):
    return self.internalArray.__str__()

hashtable = Hash(127)
hashtable.put("Ant", "Small insect!")
hashtable.put("Termite", "Rivals of ants!")
hashtable.put("Sea", "Nice view!")
hashtable.get("Termite")

print(hashtable)