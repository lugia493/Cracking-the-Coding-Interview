# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:49:26 2019

@author: Daniel
"""

def URLify(str):
    newString = []
    for char in str:
        if char == ' ':
            newString.append('%')
            newString.append('2')
            newString.append('0')
        else:
            newString.append(char)
    print(''.join(newString))
    return

def main():
    str = ["Mr", "John", "Smith"]
    print(len(str))
    URLify(str)
    
    print(" ".join(str))
main()