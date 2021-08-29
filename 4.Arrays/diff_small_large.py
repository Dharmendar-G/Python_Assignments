# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:11:13 2021

@author: dharmendar
"""

# function to get the difference of largest and smallest value

def difference(small, large):
    diff = large - small
    print(diff)
    
difference(20,80)

# difference of largest and smallest values in an array

def difference(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    small = arr[0]
    large = arr[-1]
    diff = large - small
    print(diff)
    
arr = [1,2,10,20,30,40,50,70,80,100]

difference(arr)