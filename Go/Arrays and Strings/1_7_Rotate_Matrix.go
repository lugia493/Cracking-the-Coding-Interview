package main

import "fmt"

func rotateMatrix (matrix[3][3] int) [3][3]int {

	n := len(matrix)

	for level := 0; level < n/2; level++ {
		first := level
		last := n - 1 - level
		for i := first; i < last; i++ {
			offset := i - first
			top := matrix[first][i]
			matrix[first][i] = matrix[last - offset][first]
			matrix[last - offset][first] = matrix[last][last - offset]
			matrix[last][last - offset] = matrix[i][last]
			matrix[i][last] = top
		}
	}
	return matrix
}

func main() {
	matrix := [3][3] int {{1,2,3},{4,5,6},{7,8,9}}
	size := 3

	newMatrix := rotateMatrix(matrix)
	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			fmt.Print(newMatrix[i][j])
		}
		fmt.Println()
	}
}