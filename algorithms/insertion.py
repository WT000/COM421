# Insertion sort function takes in the array
def insertionsort(arrayinput):
    # Loop through the array starting from the first index
    # going to the final index
    for divider in range(1, len(arrayinput)):
        
        # If the index is lower than the previous index, it means
        # the previous index isn't sorted, we need to sort it!
        if arrayinput[divider] < arrayinput[divider-1]:
          
          # Counter for the while loop
          counter = divider
          
          # Until the counter reaches the end of the array and
          # the number at the counter has a value lower than the data
          # to the left, 'shift' (swap) the items in the array
          # until it's in a sorted position.
          while (counter > 0 and arrayinput[counter] < arrayinput[counter-1]):
            temp = arrayinput[counter-1]
            arrayinput[counter-1] = arrayinput[counter]
            arrayinput[counter] = temp
            counter -= 1

    # Once all data in the array has been sorted, return the
    # array
    return arrayinput

array_to_sort = [17, 5, 64, 1, 42]
print(insertionsort(array_to_sort))