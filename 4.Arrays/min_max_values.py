# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:47:43 2021

@author: dharmendar
"""

# function to find the minimum and maximum value of an array

def min_max(arr):
    min = arr[0]
    max = arr[0]
    
    for i in range(len(arr)):
        if(arr[i]<min):
            min = arr[i]
        else:
            continue
        
    for j in range(len(arr)):
        if(arr[i]>max):
            max = arr[i]
        else:
            continue
    return print(f"Min value:{min} \nMax value:{max}")
    
arr = [12,16,8,20,39,40,16,55,80]

min_max(arr)