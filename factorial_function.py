#Factorial function

#Iterative implementation

def factorial_i(n):
  answer = 1
  while n > 1:
    answer *= n
    n -= 1
  return answer

#i.e n=5
#answer = 1
#answer =  5 * 1
#n = 5-1
#answer = 5 * 4
#n = 4-1
#answer = 20 * 3
#n = 3-1
#answer = 60 * 2
#n = 2-1
#answer = 120
#answer = 120*1
#n = 1-0
#answer = 120


def factorial(n):
  result = 1

  for n in range(1, n+1):
    result *= n
  return result


#Recursive implementation

def factorial_r(n):
  if n <= 1:
    return 1
  else:
    return n * factorial_r(n-1)


print(factorial_r(5))
print(factorial_i(5))
print(factorial(5))
