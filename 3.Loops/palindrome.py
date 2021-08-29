# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:30:38 2021

@author: dharmendar
"""

# Palindrome or not

def IsPalindrome(word):
    # reverse 
    r_word = word[::-1]
    
    if(word==r_word):
        print(word, 'is a Palindrome')
    else:
        print(word, 'is not a Palindrome')
        
IsPalindrome('madam')

IsPalindrome('level')

IsPalindrome('python')

