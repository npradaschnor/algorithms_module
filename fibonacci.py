#Fibonacci series can be use to model the growth rate of organisms
#e.g. leaf arrangements in plants, proportions of human body, the scales of a pineapple, number of petals on a flower
# sequence is 0,1,1,2,3,5,etc  the following number is the sum of the previous 2 nummbers

#Itineration

def fib(n):
  i,n1,n2 = 1,0,1

  while i < n:
    temp = n1 #stores previous number in the sequence
    n1 = n2
    n2 = n1 + temp
    i += 1
  return n1


print(fib(5))

#Example of Binary recursion as it calls itself twice that is: fib_rec(n-1) and fib_rec(n-2). It is NOT a tail rec, as the last return is the sum of the last 2 returns

def fib_rec(n):
  if n == 1:
    return 0
  elif n ==2:
    return 1
  return fib_rec(n-1)+fib_rec(n-2)

print(fib_rec(5))