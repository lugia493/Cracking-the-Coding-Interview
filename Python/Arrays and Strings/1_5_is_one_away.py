# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:49:22 2019

@author: Daniel
"""


#runtime 0(m + n)

def one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        print("Not One Away")
        return
    
    if len(str1) > len(str2):
        bigger_str = str1
        smaller_str = str2
    else:
        bigger_str = str2
        smaller_str = str1
    #Case 1: str1 and str2 lengths are equal
    i = 0
    only_one_away = False
    
    if len(str1) == len(str2):
        while i < len(str1):
            if str1[i] != str2[i]:
                if only_one_away == True:
                    print("Not One Away")
                    return
                else:
                    only_one_away = True
            i = i + 1
        if only_one_away == True:
            print("is one away")
            return
        else:
            print("is not one away")
            return
    else:
        j = 0
        while j < len(smaller_str):
            if bigger_str[i] != smaller_str[j]:
                if only_one_away == True:
                    print("Not one away")
                    return
                else:
                    j = j - 1
                    only_one_away = True
            i = i + 1
            j = j + 1
        print("is one away")
        return

def main():
    str1 = "pale"
    str2 = "ple"
    
    str3 = "pales"
    str4 = "pale"
    
    str5 = "pale"
    str6 = "bake"
    
    inputs = (str1, str2, str3, str4, str5, str6)
    for i in range(5):
        one_away(inputs[i], inputs[i+1])
main()
