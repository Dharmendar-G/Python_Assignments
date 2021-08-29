# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:03:03 2021

@author: dharmendar
"""

# function to find the duplicate values of an array

def duplicates(arr):
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if(arr[i]==arr[j]):
                print('Duplicate :',arr[i])
                
arr = [1,2,2,3,4,5,6,6,7,8,9,9]

duplicates(arr)
        