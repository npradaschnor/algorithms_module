def stringRev (word):
  worLen = len(word)
  if worLen == 1:
    return word
  else:
    return [word[-1]] + stringRev(word[:-1])

print(stringRev('Capaz'))