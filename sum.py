#sum the elements of an array

def sumArray(array):
  e = len(array)
  if e == 1:
    return array[0]
  
  else:
    return array[0]+ sumArray(array[1:])

a = range(10)

print(sumArray(a))

#testing with a builtin function
print(sum(a))