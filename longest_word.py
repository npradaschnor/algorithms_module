

def longest(txt): #function that returns the longest word in a sentence

  text = list(txt.split()) #separate the sentence by words 
  length = 0 #length of the word
  longest = '' #will store the longest word of the sentence

  for w in text: #for each word in the sentence
     if len(w) > length: #if the length of the word is bigger than the variable length
          longest = w #then the variable longest store that word
          length = len(w) #and the varuable length get the balue of the length of that word, so the length of next word will be compared to this updated value
     else: 
          continue
  return longest #after looping through the list, return the last word stored in the longest variable


txt = "Python is a programming language that lets you work quickly and integrate systems more effectively"
print(longest(txt))

def longest_sorted(txt)


  text = txt.split()
  sortedText = sorted(text, key=len)
  print(sortedText[-1])
    

