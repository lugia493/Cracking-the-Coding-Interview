# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 22:35:36 2019

@author: Daniel
"""
def rotate_matrix(matrix):
    levels = int(len(matrix[0]) / 2)
    for level in range(0, levels):
        first = level
        last = len(matrix[0]) - 1 - level
        temp = 0
        for offset in range(first, last):
            temp = matrix[first][first + offset]
            matrix[first][first + offset] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset]= matrix[first + offset][last]
            matrix[first + offset][last] = temp    
    print(matrix)
    return
    
def main():
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    
    #matrix[row][col]
    rotate_matrix(matrix)

main()