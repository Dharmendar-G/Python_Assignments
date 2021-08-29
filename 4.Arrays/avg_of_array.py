# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 15:39:53 2021

@author: dharmendar
"""

def array_avg(arr):
    n = len(arr)
    sum = 0
    for i in arr:
        sum += i
    
    avg = sum/n
    print(avg)

arr = [1,2,5,8,33,23,6,89,13,18]

array_avg(arr)