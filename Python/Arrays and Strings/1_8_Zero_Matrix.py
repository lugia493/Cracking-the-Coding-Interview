# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:58:24 2019

@author: Daniel
"""

def zero_matrix(matrix):
    isZeroRow = False
    isZeroCol = False
    
    for val in matrix:
        if val == 0:
            isZeroRow = True
    for val in matrix[0]:
        if val == 0:
            isZeroCol = True  
            
    for i in range (1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if (matrix[i][0] == 0) or (matrix[0][j] == 0):
                matrix[i][j] = 0
                
    if isZeroRow:
        for i in range(0, len(matrix)):
            matrix[i][0] = 0
    if isZeroCol:
        for j in range(0, len(matrix[0])):
            matrix[0][j] = 0
            
    print(matrix)
    return
            
    
    
    
    
def main():
    matrix = [[1,2,0],[4,0,6],[7,8,9], [10,11,12]]

    zero_matrix(matrix)
main()