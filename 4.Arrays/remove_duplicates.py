# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 19:05:11 2021

@author: dharmendar
"""

# Method to remove duplicate elements from an array

def remove_duplicates(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    
    print(new_arr)
    
arr = [1,2,1,1,3,3,4,1,5,6,6,7,8,9]

remove_duplicates(arr)