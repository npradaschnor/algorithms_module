# check for duplicate number in an array

def duplicate(array):

  for i in range(0,len(array)):
    for j in range(0,len(array)):
      if i == j: #avoid self comparison
        continue
      if array[i] == array[j]:
          return True #duplicate found
    return False

array = [1,45,78,63,92,1]
element = [85,96,25,32,74,25,10,52,75,35,45,45]

print(duplicate(array))
print(duplicate(element))