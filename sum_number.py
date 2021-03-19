#function that sums up all the digits in a given number

#recursive function

def sum_number(n):

  if n ==1 or n == 0:
    return n
  
  else:
    return sum_number(n // 10) + (n % 10) #n//10 is the number not including the last digit + n%10 (the last digit)

#print(sum_number(8547935))
#print(8+5+4+7+9+3+5) #testing

#iteration

def sum_digit(number):

  sumall = 0 #variable that stores the sum of all digits of the number
  digits = [int(d) for d in str(number)] #list that contains each digit of the number as element

  if number == 1 or number == 0:
    return number
  
  for digit in digits: #digit = each digit of the number
    sumall = sumall + digit

  return sumall


print(sum_digit(8547935))
