package main

import (
	"strings"
	"fmt"
)

func PP(str string) bool {

	//Process string
	str_processed := ""
	for i, v := range str {
		if string(v) == " " {
			i++
		} else {
			str_processed += strings.ToLower(string(v))
		}
	}

	var arr[26] int
	for _, v := range str_processed {
		if arr[v - 97] == 1 {
			arr[v - 97] -= 1 
		} else {
			arr[v - 97] += 1
		}
	}

	foundOne := false
	for i := 0; i < len(arr); i++ {
		if arr[i] == 1 && foundOne == false {
			foundOne = true
		} else if arr[i] == 1 && foundOne == true {
			return false
		}
	}

	return true
}

func main() {
	str1 := "Tact Coa"
	fmt.Println(PP(str1))
}