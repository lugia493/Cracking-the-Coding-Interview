package main 

import "fmt"

func zero(matrix[][] int, size int) bool {
	if len(matrix) == 0 {
		return false
	}
	
	var row = make([]bool, size)
	var col = make([]bool, size)

	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			if matrix[i][j] == 0 {
				col[i] = true
				row[j] = true
			}
		}
	}
	for j := 0; j < size; j++ {
		if row[j] == true {
			for i := 0; i < size; i++ {
				matrix[i][j] = 0
			}
		}
	}
	
	for i := 0; i < size; i++ {
		if col[i] == true {
			for j := 0; j < size; j++ {
				matrix[i][j] = 0
			}
		}
	}

	return true
}

func main() {
	matrix := [][] int {{1,4,1},{9,8,6},{0,7,9}}
	size := len(matrix)

	fmt.Println(zero(matrix, size))
	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			fmt.Print(matrix[i][j])
		}
		fmt.Println()
	}


}