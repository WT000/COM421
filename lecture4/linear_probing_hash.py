# The Hashtable class that will have 3 methods, hash, put and get
class Hashtable:
  def __init__(self, size=127):
    self.size = size
    self.bucket_list = [None] * self.size # The size at default is 127, but can be changed based on user input

  # We can use a hash function that takes the key to stop us from repeating the hash code
  def hash(self, key):
    # Control variables
    hash_total = 0
    counter = 0
    
    # Go through each character in the key and perform the hashing function
    for character in key:
      hash_total += ord(character)*(31**counter)
      counter += 1
    hash_total %= self.size
    
    # Return the hashed value
    return hash_total
  
  # This function will add a key and value in the underlying list
  def put(self, key, value):
    # Call the hash function and store the return in a variable
    finished_hash = self.hash(key)
    
    # If the index is None, we can immediately make it the bucket
    if (self.bucket_list[finished_hash] == None):
      self.bucket_list[finished_hash] = (key, value)
    
    # However, if we cant't, it means we need to find an empty
    # space through a loop
    else:
      newpos = finished_hash + 1

      while (newpos is not finished_hash):
        if (newpos == self.size):
          newpos = 0
        if (self.bucket_list[newpos] == None):
          self.bucket_list[newpos] = (key, value)
          return True
        else:
          newpos += 1
      
      print("No buckets available.")
      return None

  # This function allows a user to enter a key to view its associated value
  def get(self, key):
    # Hash the key and then get the bucket at the index
    finished_hash = self.hash(key)
    fetched_bucket = self.bucket_list[finished_hash]

    # If there's nothing, return None
    if (fetched_bucket == None):
      return None
    
    # If we find the key, return the value
    elif (fetched_bucket[0] == key):
      return fetched_bucket[1]
    
    # If the key is not there then there's been a collision or
    # the bucket doesn't exist
    # Go through each bucket and look for the key within any that
    # aren't None, otherwise return None
    else:
      newpos = finished_hash + 1
      
      while (newpos is not finished_hash):
        if (newpos == self.size):
          newpos = 0
        elif (self.bucket_list[newpos] is not None):
          templist = self.bucket_list[newpos]
          if (templist[0] == key):
            return templist[1]
        newpos += 1

      return None
    
  def __str__(self):
    return self.bucket_list.__str__()

words = Hashtable(20)
words.put("cat", "mammal that meows")
words.put("act", "doing something")
words.put("turtle", "shelled animal")
words.put("lion", "angry cat")
words.put("sea", "the ocean")
print(words)
print(words.get("turtle"))