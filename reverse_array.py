#Write an algorithm that returns a new array which is the reverse of the input.

#Option 1
def reverse_array(array):

  a = len(array) #number of elements in the array
  i = - 1 #to get the last element of the array, variable that will be the index of the array in the for loop
  new = [] #empty list to be populate with reversed array

  for n in range(0, a): 
    n = array[i] 
    new.append(n) #add the element in the new array
    i -= 1 #reduce the index by one to get the next element in the 'left' direction

  return new

#Option 2
def reverse_again(array):
  new_array = array[::-1] #using slicing
  return new_array

# Option 3 by Dominic Carr (Lecturer - Algorithmics Module)
def reverse_module(input):
    output = []
    index = len(input)-1
    while (index >= 0):
        output.append(input[index])
        index -= 1

    return output

arrayLetters = ['A', 'I', 'R', 'A', 'M']
arrayNumbers = [2, 4, 0, 1, 3, 5, 10, 52, 85, 14, 38, 60, 74, 8, 21]
arrayMixed = ['I', 2, 'LOVE', 'U', 10, 2, 'BR']

#print(reverse_array(arrayLetters))
#print(reverse_again(arrayNumbers))
#print(reverse_module(arrayMixed))

#recursive function


def insert_symbol(string):
  l = len(string)-1
  new_string = '|'.join(string[i:i + 1] for i in range(0, len(string), 1))

  if l == 0 | 1:
    return string

  else:
    return str(new_string)

print(insert_symbol('amada'))

def reverse_string(string):
  string = list(string)
  s = len(string) #length of the string
  s0 = string[0] #first letter of the string
  
  if s == 1: #base code
    return string #if the string has only 1 letter, return the string itself
  
  else: #else
    reverse = reverse_string(string[1:]) + [s0] #the function calls itself and adds in the end the first letter of the string

    return ['|'.join(reverse[0: s])]

print(reverse_string('GMIT'))
