# Longest substring in alphabetical order
"""
Created on Mon Aug 29 18:24:34 2022

@author: Mikey_I_G
"""

s = str(input('Enter a string of letters: '))
alphabet = str('') # - Placeholder for string of letters in alphbetical order
alphabetical = str('') # - Longest string of letters in alphbetical order
alphNumHist = 0 # - Numerical value of the Last letter past through the alpha string

for char in s: # - char is the letter of the given s-string in any given itteration
    alphNum = 0 # - alpha itteration counter, gives a numerical value to a letter of the alphabet
    
    for alpha in 'abcdefghijklmnopqrstuvwxyz': # - alpha is the letter of the alphabet in any given itteration
       
        alphNum += 1 # - Counter to allow recall of last letter
        
        if char == alpha: # - If the letter in char loop is the same as the letter in the alpha loop then procede 
           
            if alphabet == str(''): # - If there are no letters preceding the ie the alphbet string is still empty then procede in this statment
                alphabet = char 
                alphNumHist = alphNum 
                alphabetical = char
                
            elif alphNum - alphNumHist >= 0 : # - If the previous new letter is greater or equal to the previous leter, ie falls further down the alphabet, then procede
                alphabet += char
                alphNumHist = alphNum            
                
                if len(alphabet) > len(alphabetical):
                    alphabetical = alphabet      
            
            else:
                alphabet = char
                alphNumHist = alphNum

print('Longest substring in alphabetical order is: ' + alphabetical)