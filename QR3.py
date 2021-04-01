#Q1. Write a method to to take in a string and return a new string where all the duplicated adjacent characters have been removed. For example "AAABBBBCCCDDDD" would yield "ABCD".Must be done using recursion


def duplicates(string):
  n = len(string) #length of the string
  if n == 1: #if the string got just one letter, return the string itself
    return string
  else: #if the string has more than 1 letter, then
    if string[0] == string[1]: #if the first letter is the same as the second letter
      return duplicates(string[1:]) #check the second letter with the next one and so on
  return string[0] + duplicates(string[1:]) #then return the first letter and the ones not duplicated


test = 'AAABBBBCCCDDDD'
test2 = 'DDDDomiiiiinnnnniccccc'
print(duplicates(test2))

#Q2. Provide an implementation of Bubblesort as per the below method signature
def sort(arr):

  n = len(arr) #length of arr

  for element in arr: #loop through the arr
    for index in range(0,n-1):#get the index of arr (will 'get' the index of all the elements in the arr)
      if arr[index] > arr[index+1]:#if an element in a specific index is bigger than the next element
        temp = arr[index] #a temporary variable gets the value of the bigger element
        arr[index] = arr[index+1] #the variable with the bigger value gets the value of the smallest element
        arr[index+1] = temp #the smallest value variable gets the value of temp variable
  return arr 

a = [64, 34, 25, 12, 22, 11, 90]
array = [64, 34, 11, 456, 12, 11, -10]
print(sort(a))
print(sort(array))

#Q3.Write a method which accepts two lists/arrays of numbers. The method should return the sum of the indexes of all the elements of the second array found in the first array. For example given [42, 12, 21, 30] and [12, 30] the result would be 1+3=4. -1 should be used when a element is not found.

def sum_indexes(arr, arr2):
  indexes = [i for i, item in enumerate(arr) if item in arr2] #return index of all elements in arr that are in the arr2 as well

  diff = list(set(arr2) - set(arr)) #get the elements of arr2 that are not in arr
  size = int(len(diff)) #number of elements in arr2 that are not in arr
  sumIndexes = sum(indexes) #sum of the index of the elements of arr1 that are in the arr2

  if size > 0: #if there is an element in arr2 that is NOT in the arr, then
    finalSum = sumIndexes - size #subtract the sum of indexes
    return finalSum
  if size == 0:#if all the elements in arr2 are in arr, then
    return sumIndexes #no need to subtract

print(sum_indexes(a,array))

a1 = [42, 12, 21, 30]
a2 = [12, 30, 45]


print(sum_indexes(a1,a2))

x = [42, 12, 21, 30]
y = [12, 30]

print(sum_indexes(x, y))
