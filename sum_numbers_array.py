#Write an algorithm that computes the running total of an array of numbers.

#Option 1 using sum funtion
def sum_all(array):

  #for i in range(0, len(array)):
    return sum(array)
        

array = [1,2,3,4,5]

sum = sum_all(array)
print("The sum of all numbers in the array is"+" "+str(sum))

array = [1, 2, 3, 4, 5]

# Option 2 after watching the pseudocode video
def sumGMIT(array):
  n = 0
  sum = 0

  for i in array:

    if n == len(array):
      break

    else:
      sum += int(i)
      n += 1
  return sum

print(sumGMIT(array))

# Option 3 by Dominic Carr (Lecturer - Algorithmics Module)
def sum(input):
    total = 0
    for i in input:
        total += i

    return total


print(sum([1, 2, 3, 4]))
