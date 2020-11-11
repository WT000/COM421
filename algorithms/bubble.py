# A list of numbers which will be supplied to bubble sort
list_of_n = [20, 39, 48, 10, 8, 3]

# The sorting algorithm itself will need to be ran n-1 times, so
# we can use a for loop to do this
for i in range(len(list_of_n) - 1):
  
  # Then, for each number inside the list of numbers - 1 and - i
  # (so we don't keep going to numbers we've already sorted), we
  # swap the position of j  with anything that's bigger than it
  # TO THE RIGHT.

  # The minus i part could be seen as making this as a modified
  # bubble sort
  for j in range(len(list_of_n) - 1 - i):
    if (list_of_n[j] > list_of_n[j+1]):
      temp = list_of_n[j]
      list_of_n[j] = list_of_n[j+1]
      list_of_n[j+1] = temp

print(list_of_n)