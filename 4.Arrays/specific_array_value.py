# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:15:00 2021

@author: dharmendar
"""

# function to test if array contains a specific value

def array_contains_value(arr,x):
    for i in range(len(arr)):
        if(arr[i] == x):
            return print(True)
    return print(False)
    
arr = [1,2,3,5,6,7,8]

array_contains_value(arr, 4)

array_contains_value(arr, 6)