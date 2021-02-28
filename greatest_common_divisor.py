#Greatest Common divisor: largest positive integer which divides into both numbers without leaving a remainder

#Iterative implementation

def gcd_i(a,b):
  while b!= 0:
    temp = b
    b = a % b
    a = temp
  return a

#temp = 49
#b = 35
#a = 49

#temp = 35
#b = 14
#a = 35

#temp = 14
#b = 7
#a = 14

#temp = 7
#b = 0
#a = 7

#Recursive implementation

def gcd_r(a,b):
  if b==0:
    return a
  else:
    return gcd_r(b, a%b) #function calling itself

#gcd_r(49,35)
#gcd_r(35,14)
#gcd_r(14,7)
#gcd_r(7,0)

print(gcd_i(35,49))
print(gcd_r(35,49))