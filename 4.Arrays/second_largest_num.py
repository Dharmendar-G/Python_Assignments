# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 19:14:58 2021

@author: dharmendar
"""

# Method to find the second largest number in an array

def second_large_num(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    second_max = arr[-2]
    print(second_max)

arr = [1,2,10,20,30,40,50,70,80,100]

second_large_num(arr)