import math

def binarysearch(number):
  # Firstly we create a number list and then create
  # references to the start and end of the list,
  # we also make found set to false
  number_list = [i*i for i in range(1, 101)]
  start_index = 0
  end_index = len(number_list)
  found = False

  # While found is false and the start is not equal to
  # the end minus 1 (meaning we've got nowhere else
  # to look for), work out the middle of the array
  # and see if the number is present.

  # If the number is lower than the middle, we set
  # the endpoint to the middle index
  # If the number is greater than the middle, we set
  # the startpoint to the middle index
  while (found == False and start_index != end_index-1):
    middle = math.floor((start_index + end_index) / 2)

    if (number_list[middle] == number):
      found = True
    elif (number < number_list[middle]):
      end_index = middle
    elif (number > number_list[middle]):
      start_index = middle
  
  # If we found the number, we print the number and
  # the index number, else we say it couldn't be
  # found.
  if (found == True):
    print("{} was found at index {}".format(number, middle))
  else:
    print("Couldn't find {} in the list".format(number))
  
def program():
  number_to_find = int(input("Enter a number you want to find: "))
  binarysearch(number_to_find)

program()