#Write an algorithm that returns the largest element in an array. 
#Assume the array is unsorted.

#Option 1
def largest(array):
 

    max = array[0]  # first element of array

    for i in range(0, len(array)):  # Loop through the array
       
            if(array[i] > max):  # Compare elements of array with max
               max = array[i] #the variable max becomes the element that is larger than it
    return max #return the last value of max
        

array = [25, 6, 99, 74, 20, 101]

large = largest(array)
print("The largest number in the array is"+" "+str(large))

#Option 2 by Dominic Carr (Lecturer - Algorithmics Module)
def largest(input):
  	largest = input[0]
	for i in input:
		if i>largest:
			largest = i
	
	return largest
    
print(largest([1,2,888,12,84,9]))
