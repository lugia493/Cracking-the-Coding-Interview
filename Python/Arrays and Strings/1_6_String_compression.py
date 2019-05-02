# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:59:12 2019

@author: Daniel
"""


def string_compression(input_string):
    result = ""
    char = ''
    count = 0
    i = 0
    j = 0

    while i < len(input_string):
        if input_string[i] == input_string[j]:
            char = input_string[i]
            i += 1
            count += 1
            if i == len(input_string) - 1:
                result += char +  str(count)
                char = input_string[i]
                count = 1
        else:
            result += char +  str(count)
            count = 0
            j = i
    if len(result) > len(input_string):
        print(input_string)
    else:
        print(result)
    return


def main():
    input_string = "abcccccaaabcfsddsdddfffffz"
    input_string2 = "abc"
    string_compression(input_string)
    string_compression(input_string2)

    
main()