# A list of values that need to be sorted
values = [5, 5, 5, 4, 3, 3, 1]

# The first loop goes through the entire array length-1 times.
for comparing_index in range(len(values) - 1):
  # Set (or reset) the current_lowest value by making it the 
  # comparing index
  current_lowest = comparing_index
  
  # Then, we loop through each entry in the index starting from
  # the comparing index + 1
  for current_index in range(comparing_index+1, len(values)):
    
    # If the value in the current index is lower than the current
    # lowest, we update which index holds the smallest value
    if (values[current_index] < values[current_lowest]):
      current_lowest = current_index
  
  # Once we've gone through each index, if the values are not
  # the same, we swap them
  if (values[comparing_index] != values[current_lowest]):
    temp = values[comparing_index]
    values[comparing_index] = values[current_lowest]
    values[current_lowest] = temp

# Print the updated list
print(values)