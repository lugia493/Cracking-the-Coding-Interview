package main

import "fmt"

func isUnique(str string) bool {

	var arr [26]int
	for _, char := range str {
		if arr[char - 97] == 1 {
			return false
		}
		arr[char - 97] = 1		
	}
	return true
}

func main(){
	PolarQuestion := isUnique("abcdefghijklmnopqrstuvwxyz") //works for only lower case letters. Increase array for all letters

	if PolarQuestion == false {
		fmt.Println("Not Unique")
	} else {
		fmt.Println("Unique")
	}
}