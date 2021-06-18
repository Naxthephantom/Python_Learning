
#Binary search algorithm
def binary_search(number, item):
    left = 0
    right = len(number) - 1
    
    while left <= right:  
      middle = int((left + right) / 2) # middle tile
    
      if item < number[middle]:
        right = middle - 1             
      elif item > number [middle]:
        left = middle + 1
      else:
        return middle
    
 #I'm going to set down the basic parameters the algorithm is going to be using
size = 100000000                      #The total numbers the code is searching through (the hay stack)
ordered_list = range(0, size) 
search_item = 5426998                 #the number we are looking for (the needle)

#now im setting the parameters in line with my biniary search formula under the name found_index
found_index = binary_search(ordered_list, search_item)

if found_index != -1:
    print("found: ", found_index)
else:
    print("Not found")
    
