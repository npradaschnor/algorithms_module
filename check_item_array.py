#Write an algorithm that checks whether an element occurs in an array



def check(i):

  array = [1, 89, 52, 47, 60, 20, 7, 25, 85, 101, 3, 10]

  for e in array:
    if e == i:
      print("The number is in the array.")
      break
  
    else:
      continue
  print("If you haven't got a message yet, the number is NOT in the array.")


print(check(20))
