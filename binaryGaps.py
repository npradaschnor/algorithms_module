
def solution(N):

  binary = str(bin(N))[2:]
  counterZero = 0
  counterLongest = 0

  for digit in binary:
        if digit == '1':
          if counterLongest < counterZero:
            counterLongest = counterZero
          counterZero = 0

        if digit == '0':
          counterZero += 1
  print(counterLongest)
  
solution(37)
solution(1041)