# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 15:07:51 2021

@author: dharmendar
"""

# Scope of Global and local variables

# Global variables 
name = 'dharmendra'
print(name)

def func():
    print(name)

func()

# Local variable
def local_var():
    name = 'Python'
    
    global local_name
    local_name = 'global'
    print(f"Local Variable: {name} \nLocal variable as Global: {local_name}")
    
    
local_var()

print(local_name)

# Scope of the variables 
'''
Global Variable : Any variable defined outside the function is a global variable and,
                  It can be accessed any where in the program and 
                  we can also declare a global variable inside the function with global keyword
            
Local Variabel : A variable which is defined inside the function is called a local variable and
                 it can not be accessed outside the function and 
                 we can make a local variable as global with the keyword global