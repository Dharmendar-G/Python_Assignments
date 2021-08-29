# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:43:21 2021

@author: dharmendar
"""

# Check if the number is an Armstrong number or not

# user input
num = int(input("Enter a number: "))

sum = 0
# sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
