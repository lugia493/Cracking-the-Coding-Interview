# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:23:22 2019

@author: Daniel
"""
def isPermutation(str1, str2):
    test = set(str1 + str2)
    if len(test) == len(str1):
        print("is permutation")
    else:
        print("is not permutation")
    return

def main():
    str1 = "ABC"
    str2 = "BAC"
    isPermutation(str1, str2)
main()