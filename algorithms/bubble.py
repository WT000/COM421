# A list of numbers which will be supplied to bubble sort
list_of_n = [20, 39, 48, 10, 8, 3]

# The sorting algorithm itself will need to be ran n-1 times, so
# we can use a for loop to do this
for i in range(len(list_of_n) - 1):
  
  # Swap the positions of an item in the index if j is greater
  # than j+1
  for j in range(len(list_of_n) - 1 - i):
    if (list_of_n[j] > list_of_n[j+1]):
      temp = list_of_n[j]
      list_of_n[j] = list_of_n[j+1]
      list_of_n[j+1] = temp

# Print the sorted list
print(list_of_n)