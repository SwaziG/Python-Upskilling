# How many times does 'bob' occour in the string
"""
Created on Mon Aug 29 12:46:44 2022

@author: Mikey_I_G
"""

s = str(input('Input a phrase: '))

bobs = 0 
itt= 0

for char in s:
    ThrL = str(s[itt:itt + 3])
    if ThrL == 'bob':
        bobs += 1
    itt += 1
        
print('Number of times bob occurs is: ' + str(bobs))
