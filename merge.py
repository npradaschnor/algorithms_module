#recursive function that returns a merged list (1 element of str1 + 1 element of str2...and so on)
def merge(str1,str2):

  if len(str1) == 0: #if the number of element in the str1 is zero, return str2
    return str2
  elif len(str2) == 0:  # if the number of element in the str2 is zero, return str1
    return str1
  
  else:
    return str1[0] + str2[0] + merge(str1[1:],str2[1:]) #first element of str1 + first element of str2 + function calling itself to continue the pattern of element str1 + str2 to result in a merged list

print(merge('dmnc', 'oii'))
