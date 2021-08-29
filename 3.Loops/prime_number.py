# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:51:38 2021

@author: dharmendar
"""

num = int(input('Enter Number: '))

if num > 1:
    for i in range(2,(num//2)+1):
        if(num % i) == 0:
            print(num, 'is not a prime number')
            break
    else:
        print(num, 'is a prime number')
    
else:
    print(num, 'is not a prime number')
            
        
