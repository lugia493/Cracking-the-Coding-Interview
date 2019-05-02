# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:07:43 2019

@author: Daniel
"""

#0(n) time algorithm 
#n is length of the string

def isUnique(str):
    boolArr = [False] * (ord('z') - ord('A'))
    for char in str:
        if boolArr[ord(char) - ord('A')] == True:
            print("Not Unique")
            return
        else:
            boolArr[ord(char)- ord('A')] = True
    print("Is Unique")
    return 

def main():
    str = "Dajifbcenw"
    print(ord('9'))
    isUnique(str)
main()