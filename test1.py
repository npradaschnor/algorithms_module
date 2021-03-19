#recursive function that returns the reverse of the string with the symbol '|' on the right side of the letter (except the last one)
def reverse_string(string):
  string = list(string)
  s = len(string)  # length of the string
  s0 = string[0]  # first letter of the string

  if s == 1:  # base code
    return string  # if the string has only 1 letter, return the string itself

  else:  # else
    # the function calls itself and adds in the end the first letter of the string
    return reverse_string(string[1:]) + ['|'] + [s0]

print(reverse_string('GMIT'))
