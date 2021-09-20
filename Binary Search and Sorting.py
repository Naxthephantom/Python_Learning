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
    

words = [ 'a', 'b', 'c']
def sorting(words):
   for i in range(0,len(words)):
    for j in range(0,len(words)):
        if words[j] > words[i]:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp
    
    return words   


ordered_list = [54, 86, 800, 45, 10, 152, 134, 516]

words = ordered_list
sorting(words)
for i in range(0,len(words)):
    for j in range(0,len(words)):
        if words[j] > words[i]:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp
    
print(words) 

Result_index = binary_search(ordered_list, 134)
if Result_index != -1:
    print("found: ", Result_index)
else:
    print("Not found")
