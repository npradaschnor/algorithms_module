#recursive function that return the string converted into a list and excludes any 'extra' elements if the length of the list is not 'divisable' by 3
def string_three(string):
  #string = [i for j in list(string) for i in (j)]
  string = list(string) #convert string in list

  length = len(string)
  remainder = length % 3
  dif = length - remainder #dif is the different between the length of the list and the remainder of length / 3

  if length % 3 != 0: #if the number of elements of the list is not 'divisabe' by 3
    string = string[0:dif] #string will contain the first element to the dif to become a list 'divisable' by 3
    return string 
  else: #if the length of the list is 'divisable' by 3 the list itself is returned
    return string

#recursive function that return the 'string' in chunks of 3 (including spaces). If the last chunk does not contain 3 elements, it should be excluded
def substrings(string):
  string = string_three(string) #if the length of the list is not 'divisable' by 3 this function will return a list which the number of elements is divisable by 3
  length = len(string)

  if length <=2: #base code
   return string
  else:
    first = string[0]+string[1]+string[2] #first 'chunk' of 3 elements merged
    rest = string[3:length] #list excluding the first 3 elements
    result =  [first] + substrings(rest) #first 3 elements merged + call the function itself passing the 'rest' of the list
  return result


string = 'We are in isolation'
print(substrings(string))
