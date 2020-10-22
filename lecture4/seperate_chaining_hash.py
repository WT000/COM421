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
    
    # Create a list at the hash result if there's nothing there
    if (self.bucket_list[finished_hash] == None):
      self.bucket_list[finished_hash] = []
    
    # Append the key and value as a tuple into the created list
    self.bucket_list[finished_hash].append((key, value))

  # This function allows a user to enter a key to view its associated value
  def get(self, key):
    # Hash the key and then get the bucket at the index
    finished_hash = self.hash(key)
    fetched_bucket = self.bucket_list[finished_hash]

    # If there's nothing, return None
    if (fetched_bucket == None):
      return None

    # Use a for loop to go through the bucket until we find the key we're looking for
    for data in fetched_bucket:
      if (data[0] == key): # If the key (which is at position 0) is equal to the users key, print a special message and return the value.
        print("The key \"{}\" is at bucket {}.".format(key, finished_hash))
        return data[1]
    
  def __str__(self):
    return self.bucket_list.__str__()

words = Hashtable()
words.put("cat", "mammal that meows")
words.put("act", "doing something")
#print(words)
print(words.get("cat"))