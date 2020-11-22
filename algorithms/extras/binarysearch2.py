import math

def binarysearch(arraylist, to_search):
  start_index = 0
  end_index = len(arraylist) - 1
  found = False
  loop_check = 0

  while (found == False and loop_check != 1):
    middle = math.floor((start_index + end_index) / 2)

    if (start_index == end_index-1):
      loop_check += 1

    if (to_search == arraylist[middle]):
      print("{} was found at index {}".format(to_search, middle))
      found = True
    
    elif (to_search < arraylist[middle]):
      end_index = middle

    elif (to_search > arraylist[middle]):
      start_index = middle
  
  if (found == False):
    print("Couldn't find the number")

def run():
  arraylist = [i*i for i in range(1, 101)]
  print(arraylist)
  to_search = int(input("Please enter a number to search for: "))

  binarysearch(arraylist, to_search)

run()