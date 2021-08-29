# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:11:32 2021

@author: dharmendar
"""

# program to find the common values between two arrays

def common_values(arr1, arr2):
    common = []
    
    for i in range(len(arr1)):
        if arr1[i] in arr1 and arr1[i] in arr2:
            common.append(arr1[i])                
    print(common)

arr1 = [1,2,8,6,10,20,11,30]
arr2 = [2,10,20,6,7,9,25,17]

common_values(arr1, arr2)