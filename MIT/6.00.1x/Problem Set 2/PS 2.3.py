# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 17:49:19 2022

@author: Mikey_I_G
"""

balance = 999999
annualInterestRate = 0.18
high = (balance*(1+annualInterestRate))/12
low = balance/12
monthlyInterest = annualInterestRate/12
Remaining = balance

while Remaining > 0.01 or Remaining < -0.01: # Worked out to the nearest 0.01
    
    paid = 0   
    monthlypayment = (high+low)/2 # Bisectional calculation
    Remaining = balance
    
    for month in range (0,12):  # Code to work out the remaining payment after 12 months
      paid += monthlypayment
      Remaining = Remaining - monthlypayment
      Remaining += Remaining * monthlyInterest  
    
    
    if Remaining == 0: # Base Case 
        break
    
    elif Remaining > 0: # if the remaining paymening debt is higher than 0, make the low point = to the previous call
        low = monthlypayment
        
    else:               # if the remaining paymening debt is lower than 0, make the high point = to the previous call
        high = monthlypayment  
        
# balance = Remaining - Can be used if you want to re-call balance later
   
print('Lowest Payment: ' + str(round(monthlypayment,2)))