 #Write an algorithm that prints the numbers from 1 to 100 and for multiples of ’3’ print
# “Fizz” instead of the number and for the multiples of ’5’ print “Buzz”.
list = range(0,101)

for i in list:

    if i % 3 == 0 and i % 5 != 0:
      print("Fizz")
      i += 1
    elif i % 5 == 0 and i % 3 != 0:
      print("Buzz")
      i += 1
    elif (i % 3 ==0 and i % 5 == 0):
      print("FizzBuzz")
      i += 1
    elif i == 100:
      print("Buzz")
      break
    else:
      print(i)
      i += 1
    

  
