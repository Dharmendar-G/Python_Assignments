# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:36:30 2021

@author: dharmendar
"""

# function to copy an array to another array

def copy_arr(arr):
    arr2 = []
    for item in arr:
        arr2.append(item)
    print(arr2)
    
arr = [1,2,4,5,7,8,0]
copy_arr(arr)

# inbuilt function
arr2 = arr.copy()
print(arr2)
