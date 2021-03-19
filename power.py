#Given a number and a power, compute the result of the number raised to that power.
#For example 2**3 = 8.

def power(number,p): #number will be raised to the power of p

  if p == 0 or p ==1: #base code
    return 1

  else:
      return number * power(number,p-1) 

print(power(2,3))
print(power(2,5))