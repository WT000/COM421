# Import the math module for finding the midpoint
import math

# Hoare Partition function which takes 3 parameters, those being the array to be sorted,
# the starting index and the ending index
def hoarepartition(array, start_index, end_index):
    # The "fingers", i starts at the start index whilst j starts at the end index
    i = 0
    j = len(array)-1

    # Use math.floor to find the midpoint of the array
    mid = math.floor((start_index + end_index) / 2)
    
    # Infinite loop
    while True:
        # Until we get i to a number greater than the pivot, keep searching for one
        while (array[i] < array[mid]):
            i += 1

        # Once we've found the misplaced number, we do this again but for a number lower than
        # the pivot
        while (array[j] > array[mid]):
            j -= 1
        
        # Now that we've got the positions of two misplaced numbers, if i hasn't passed j,
        # we swap the values around
        if (i < j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        
        # However, if we've passed j, it means we've created the partitioned list and can return
        # the index for the pivot
        else:
            return j

# Quick sort algorithm which takes 3 parameters, an array, a starting index and an ending index
def quick_sort(array, start_index, end_index):
    # Unless the base case is met (end_index becomes lower than start_index, meaning we can't keep
    # going), find the pivot point of the given range and recursively sort the array
    if (end_index >= start_index):
        pivot = hoarepartition(array, start_index, end_index)
        quick_sort(array, start_index, pivot-1)
        quick_sort(array, pivot+1, end_index)

# Create the arra
array = [22,56,1,59,38,7,15,17,33]
quick_sort(array, 0, len(array)-1)
print(array)