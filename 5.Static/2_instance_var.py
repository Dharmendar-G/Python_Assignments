# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:10:55 2021

@author: dharmendar
"""

# 2. Define a static variable and access that through an instance

'''Variables that are initialized and accessed by an an instance of a class 
   are called instance variabels'''

# Static Variable   
class static:
    my_var = 'static variable'


# Creating Instance 
instance = static()

# Accessing through an instance  
print(instance.my_var)