class Hashtable:
  def __init__(self, size=127):
    self.size = size
    self.buckets = [None] * self.size

  def hash(self, key):
    hash_total = 0
    
    for character in key:
      hash_total += ord(character)

    hash_total %= self.size
    return hash_total
  
  def put(self, key, value):
    finished_hash = self.hash(key)
    
    if (self.buckets[finished_hash] == None):
      self.buckets[finished_hash] = []
    
    self.buckets[finished_hash].append((key, value))

  def get(self, key):
    finished_hash = self.hash(key)
    fetched_data = self.buckets[finished_hash]

    if (fetched_data == None):
      return None

    for data in fetched_data:
      if (data[0] == key):
        return data[1]
    
  def __str__(self):
    return self.buckets.__str__()

words = Hashtable()
words.put("cat", "mammal that meows")
words.put("act", "doing something")
#print(words)
print(words.get("cat"))