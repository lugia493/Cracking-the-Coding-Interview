package main

import (
	"fmt"
	"math"
)

func oneAway(str1, str2 string) bool {
	if math.Abs(float64(len(str1) - len(str2))) > 1 {
		return false
	}
	
	smallerOne := ""
	largerOne := ""
	if len(str1) > len(str2) {
		smallerOne = str2	
		largerOne = str1
	} else {
		smallerOne = str1
		largerOne = str2
	}
	
	i := 0
	j := 0
	oneAway := false
	for i < len(smallerOne) {
		if smallerOne[i] != largerOne[j] {
			if oneAway == true {
				return false
			} else {
				oneAway = true
				if len(smallerOne) - len(largerOne) != 0 {
					i--
				}
			}
		}
		i++
		j++
	} 
	return true
}

func main() {
	str1 := "pale"
	str2 := "bake"
	fmt.Println(oneAway(str1, str2))
}