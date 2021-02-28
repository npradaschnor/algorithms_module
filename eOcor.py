#Create a script which opens a file and print the number of occurences of the letter e in its content.


def eOcor(txt):  # Count the lower 'e' in the file
   
    text = txt.replace('\n', '')
    ocorrence = 0
    
    for i in text:
        for letter in i:
            if letter == 'e':
                ocorrence +=1
            else:
                continue
    print(ocorrence)
                
    
    
    
    
with open('word.txt', 'r') as f:
    txt = f.read()

eOcor(txt)
