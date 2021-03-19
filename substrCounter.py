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
string = 'A number specifying the position of the element'

#substring(sub,string)

#recursive

def substr_search(sub,str,index): #sub is the substring and str is the string, index is the length of the string
  s = len(sub) #length of the substring
  su = index - s #length of the string minus length of the substring
  counter = 0
  
  if index < s: 
    return counter
  if sub[0:s].lower() == str[su:index].lower():
    counter += 1
    return counter
  else:
    return substr_search(sub,str[su:index], index-1)

word = 'amora'
substring = 'amor'
#print(substr_search(substring,word,4))

def search(sub,str):
  return substr_search(sub,str,len(str)-1)

a = 'power'
b = 'powerless'

#print(search(a,b))


def substring_counter(str1,str2): #str1 is the substring and str2 is the string
  s1 = len(str1) #length of substring
  s2 = len(str2) #length of string
  a = 0
  str1 = str1.lower() #converting all the letter to lowercase
  str2 = str2.lower() #both string and substring are now in lowercase

  if s2 == 0 or s2 < s1: #if the length of string is zero or len of string < len of substring, return zero 
    return 0
  
  if str2[a:s1] == str1: #if the first 'chunk' of the string is the substring
    return substring_counter(str1,str2[1:]) + 1 
  
  else:
    return substring_counter(str1,str2[1:])

phrase = 'her and herself'
word = 'he'

phrase1 = 'nothing to declare'
word1 = 'clare'
print(substring_counter(word,phrase))