# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 15:42:42 2021

@author: dharm
"""

# Index of an element in the array 

arr = [1,2,6,'dog','man','cat',8,9]

print(arr.index(6))
    
print(arr.index('man'))

# without the index function
def index(arr, x):
    for idx in range(len(arr)):
        if(x==arr[idx]):
            break
    print(idx)

index(arr, 6)
index(arr, 'man')