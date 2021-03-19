#palindrome

def palindrome(word):
  #palindrome is a word that reads the same backward as forward
  reverse = word[::-1] #converting the word 'backward'

  if word == reverse:#if the 'forward' reads the same as 'backward'
    print('It\'s is a palindrome')
  else:
    print('Not a palindrome')

#test
word1 = 'civic'
word2 = 'reviver'
word3 = 'racecar'
word4 = 'saippuakivikauppias'
word4 = 'palindrome'
word5 = 'computer'

palindrome(word1)
palindrome(word2)
palindrome(word3)
palindrome(word4)
palindrome(word5)

#recursive

def is_palindrome(word):
  if word == '' or len(word) == 1:
    return True
  else:
    return word[0] == word[-1] and is_palindrome(word[1:-1]) #if the first letter = last letter then call is_palindrome from index 1 to -2 (-1 not inclusive)

print(is_palindrome(word1))
print(is_palindrome(word2))
print(is_palindrome(word3))
print(is_palindrome(word4))
print(is_palindrome(word5))