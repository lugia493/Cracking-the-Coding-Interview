package main

import "fmt"

func isSubstring(str1, str2 string) bool {
	if len(str1) != len(str2) && len(str1) > 0 {
		return false
	}

	ptr2 := -1
	for i := 0; i < len(str2); i++ {
		if str1[0] == str2[i] {
			ptr2 = i
		}
	}
	if ptr2 == -1 {
		return false
	}
	for i := 0; i < len(str1); i++ {	
		if str2[ptr2] != str1[i] {
			return false
		}
		if ptr2 == len(str1) - 1 {
			ptr2 = 0
		} else {
			ptr2++
		}
	}
	return true
}

func main() {
	str1 := "Daniel Ramsey"
	str2 := "amseyDaniel R"
	fmt.Println(isSubstring(str1, str2))
}