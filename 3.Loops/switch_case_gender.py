# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:44:41 2021

@author: dharmendar
"""

# (Male/Female) program according to given M/F using switch

def switch(x):
    gender = {1: 'Male',
                2: 'Female'}
    
    if(x=='M'):
        return print(gender.get(1, 'Option Not Available'))
    return print(gender.get(2, 'Option Not Available'))        
    
switch('M')

switch('F')