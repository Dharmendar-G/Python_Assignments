# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 15:37:02 2021

@author: dharmendar
"""

def array_sum(arr):
    sum = 0
    for i in arr:
        sum += i
    print(sum)
    
arr = [1,2,4,5,3,2,46,12,18]

array_sum(arr)