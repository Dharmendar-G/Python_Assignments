# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:27:31 2021

@author: dharmendar
"""

# Method to verify if the array contains two specified elements(12,23)

def array_contains(arr, x1, x2):
    if x1 in arr: x1 = 1
    else: x1 = 0
    
    if x2 in arr: x2 = 1
    else: x2 = 0
    
    if(x1==1 and x2==1):
        return print(True)
    print(False)
    
   
    
arr = [6,7,8,4,50,10,20,23,19,21,18,17,12]

array_contains(arr, 12, 23)

array_contains(arr, 12, 80)  
    