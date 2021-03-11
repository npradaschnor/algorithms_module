#Given a string and a substring, compute how many times that substring appears in
#the string. For example “he” appears twice in the string “her and herself”.

import re

def substring(substring,string):

  result = re.search(substring,string)

  if result:
    result2 = re.findall(substring,string)
    counter = len(result2)
    print('How many times {0} appears in {1}? The answer is: {2}'.format(substring, string,counter))

sub = 'num'
string = 'A number specifying the position of the element you want to remove.'

substring(sub,string)
