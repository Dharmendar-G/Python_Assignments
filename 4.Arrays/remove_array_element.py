# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:25:45 2021

@author: dharmendar
"""

# function to remove a specific element from an array

def remove_element(arr,x):
    new_arr = []
    for i in range(len(arr)):
        if(arr[i]==x):
            continue
        new_arr.append(arr[i])
    print(new_arr)
        
arr = [1,2,4,5,7,8,9,23,25,71,18,10]

remove_element(arr, 7)

