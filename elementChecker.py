#Write an algorithm that checks whether an element occurs in an array, assume unsorted.

def elementChecker(element,array):
  
  if element not in array:
    
    print('Sorry, {0} not in array'.format(element))
  
  else:
    print('Happy days')

a = [0,1,2,3,4,5]
elementChecker(3, a)
elementChecker(11,a)

#recursive
def linear_search(array,target,index):

  if array[index] == target: #stop if the target element was found
    return True 
  
  elif index == 0: #stop if all indexes have been checked
    return False
  
  else:
    return linear_search(array,target,index-1) #check the next element from right to left
    
def search(array,target):
  return linear_search(array,target,len(array)-1)

print(search(a,2))
