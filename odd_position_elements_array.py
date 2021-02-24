#Write an algorithm that returns the elements on odd positions in an array.

#Option 1 using 2 functions
def range_list(array):

  array = range(0,len(array))
  i = []

  for e in array:
    i.append(e)

  return i



def odd_index(array):

  oddl = []
  a = range_list(array)
  

  for n in a:
      
    if n%2 != 0: #the index cannot be even
      e = array[n] #element with index n
      oddl.append(e) #add the element in the list oddl
      n += 1 #increase index by 1
    
    elif n % 2 == 0 or n == 0: #if the index is zero or even 'skip'
      continue

  return oddl #return the list with elements that were in odd position
        

array = [25, 6, 99, 74, 20, 101]
print(range_list(array))
print(odd_index(array))

# Option 2 after watching the pseudoce video
def odd_GMIT(array):
  
  oddG = []
  
  while i <= len(array):
    for i == 1:
    oddG.append(i)
    i +=2

  return oddG

# Option 3 by Dominic Carr (Lecturer - Algorithmics Module)
def odd_indices(input):
    output = []
    for i in range(len(input)):
        if (i % 2) != 0:
            output.append(input[i])
    return output


print(odd_indices([1, 2, 3, 4, 5]))
