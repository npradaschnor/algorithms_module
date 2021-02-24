# Write an algorithm that prints a multiplication table for numbers up to 12

def multiplication_table(n):

  list = range(1,n+1) #range 1 to input value
  multi = range(1, 13) #range from 1 to 12

  for l in list: #every number from 1 to the input value in list
    for m in multi: #every number from 1 to 12
      lm = l*m # variable that stores de multiplication result from l x m
      print('{0:2d} x  {1:3d} = {2:4d}'.format(l, m, lm)) #print using the format function

multiplication_table(12) #get the multiplication table for the number 12
  

# Option 2 by Dominic Carr (Lecturer - Algorithmics Module)
def table(num, upto=13):
    for i in range(1, upto):
        print(f"{num} * {i} = {num*i}")


def all_tables():
    for i in range(13):
        print(f"Table for {i}")
        print("-----------")
        table(i)
        print("-----------")


all_tables()
