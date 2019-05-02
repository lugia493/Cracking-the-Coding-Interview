# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:24:51 2019

@author: Daniel
"""

def pal_perm(str):
    map_chars_to_array = [0] * (ord('z') - ord('a') + 1)
    for char in str.lower():
        if char == " ":
            continue
        map_chars_to_array[ord('z') - ord(char)] =   map_chars_to_array[ord('z') - ord(char)]  + 1
    
    one_and_only_one = False
    for val in map_chars_to_array:
        if val == 1:
            if one_and_only_one == True:
                print("Not a pal perm")
                return
            else:
                one_and_only_one = True
    print("Is a pal perm")
    return

def main():
    str = "Tact Coa"
    pal_perm(str)
main()