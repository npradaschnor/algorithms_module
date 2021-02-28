# Based on Caesar's Cipher

#Substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number (offset) of positions down the alphabet.
#In this case is upper in the alphabet

def encrypt(plain_text, offset):
  cipher_text = ""

  for i in plain_text: #for every char in text inputted
    numerical_value = ord(i) #unicode value of the char

    if i.isupper(): #if is uppercase
      adjusted = ((numerical_value + offset - 65) % 26) + 65 #uppercase A = 65 (ASCII). The %26 wraps around, so Y = A and Z = B
      cipher_text += chr(adjusted) #get the correspondent char
    elif numerical_value == 32: #32 = space, this intends to preserve the spaces between words
      cipher_text += i
    else: #if is lowercase
      adjusted=((numerical_value + offset - 97) % 26) + 97 #lowercase a = 97 (ASCII)
      cipher_text += chr(adjusted)

  return cipher_text


print(encrypt("hello lads", 2))
print(encrypt("are we human", 2))
