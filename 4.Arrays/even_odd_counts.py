# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 20:01:51 2021

@author: dharmendar
"""

# Method to find number of even number and odd numbers in an array

def even_odd_count(arr):
    even = 0
    odd = 0
    for i in range(len(arr)):
        if(arr[i]%2==0):
            even += 1
        else:
            odd += 1
    print(f"Even Numbers: {even} \nOdd Numbers: {odd}")
    
arr = [1,2,3,4,2,3,6,7,8,4,50,10,20,22,19,21,18,17]

even_odd_count(arr)