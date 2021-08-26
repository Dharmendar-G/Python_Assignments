# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:12:30 2021

@author: dharmendar
"""

# Increment function
def increment():
    x = int(input('Enter value of x: '))
    n = int(input("Increment 'x' by how many times': "))
    
    for _ in range(n):
        x += 1
        print(x)
        
increment()

# Decrement function
def decrement():
    x = int(input('Enter value of x: '))
    n = int(input("decrement 'x' by how many times': "))
    
    for _ in range(n):
        x -= 1
        print(x)
        
decrement()