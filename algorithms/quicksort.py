def hoare(array, startIndex, endIndex):
    # I originally used the middle of the array for the pivot, but now I'll make it the end index
    #mid = math.floor((start_index + end_index) / 2)
    pivot = array[endIndex]
    
    # Setup the i and j fingers
    i, j = startIndex, endIndex
    
    # Infinite loop
    while True:
        # While the number at i is lower than what number's at the pivot, increase i
        while array[i] < pivot:
            i += 1
        
        # While the number at j is greater than what number's at the pivot, increase j
        while array[j] > pivot:
            j -= 1
        
        # If i is lower than j, and the numbers aren't duplicates, it means we need to swap them
        if i < j and array[i] != array[j]:
            array[i], array[j] = array[j], array[i]
            
        # Else, the true index for the number at pivot has been found, return j for the next recursion of quicksort
        else:
            return j

def quickSort(array, startIndex, endIndex):
    # Start index will be lower than end index until the array is sorted, use an if statement to stop a recursion loop
    if startIndex < endIndex:
        part = hoare(array, startIndex, endIndex)
        quickSort(array, startIndex, part-1)
        quickSort(array, part+1, endIndex)

def binarySearch(array, numToFind):
    if len(array) > 1:
        leftIndex = 0
        rightIndex = len(array)-1
        
        searchIndex = None
        found = False
        while leftIndex < rightIndex and found is False:
            searchIndex = (leftIndex + rightIndex) // 2
            
            if array[searchIndex] == numToFind:
                return True
            
            elif array[searchIndex] > numToFind:
                rightIndex = searchIndex
            
            else:
                leftIndex = searchIndex
                
        return False
    
    elif array[0] == numToFind:
        return True
    
    else:
        return False

list = [22, 56, 1, 59, 38, 7, 15, 17, 33]
quickSort(list, 0, len(list)-1)
print(list)
