# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:04:50 2019

@author: Daniel
"""
def is_rotation(string_one, string_two) -> bool:
    string_two_added = string_two + string_two
    print(string_two_added)
    sliding_window = False
    i = 0
    for char in string_two_added:
        if i == len(string_one):
            return True
        elif char == string_one[i]:
            sliding_window = True
            i = i + 1
        elif char != string_one[i] and sliding_window == True:
            return False
    return False

def main():
    string_one = "waterbottle"
    string_two = "erbottlerwat"
    print(is_rotation(string_one, string_two))
main()