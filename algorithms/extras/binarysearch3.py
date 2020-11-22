def binarysearch(arraylist, to_search):
  start_index = 0
  end_index = len(arraylist) - 1

  while (start_index <= end_index):
    middle = int((start_index + end_index) / 2)

    if (to_search == arraylist[middle]):
      print("Found {} at index {}".format(to_search, middle))
      return True
    
    elif (to_search < arraylist[middle]):
      end_index = middle - 1

    elif (to_search > arraylist[middle]):
      start_index = middle + 1
  
  print("Couldn't find the number.")
  return False

def run():
  arraylist = [i*i for i in range(1, 101)]
  print(arraylist)
  to_search = int(input("Please enter a number to search for: "))

  binarysearch(arraylist, to_search)

run()