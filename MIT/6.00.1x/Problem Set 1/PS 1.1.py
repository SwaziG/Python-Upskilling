# Count the number of vowels in the string
"""
Created on Mon Aug 29 11:34:02 2022

@author: Mikey_I_G
"""

s = str(input('Input a phrase: '))

vowels = 0 

for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels += 1
print('Number of vowels: '+ str(vowels))

