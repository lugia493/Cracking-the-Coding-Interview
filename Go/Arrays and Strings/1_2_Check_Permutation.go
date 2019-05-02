package main 

import "fmt"

func isPem(str1, str2 string) {
	//Edge cases: 1 or more empty strings
	//Is str1 a palindrome of str2?

	var arr1 [26] int
	var arr2 [26] int

	if len(str1) != len(str2) || len(str1) == 0 || len(str2) == 0 {
		fmt.Println("No")
	} else {
		for _, v := range str1 {
			arr1[v - 97] += 1;
		 }
		 for _, v := range str2 {
			 arr2[v - 97] += 1;
		 }
		 if (arr1 == arr2) {
			 fmt.Println("Yes")
		 } else {
			 fmt.Println("No")
		 }
	}
	return
}

func main() {
	str1 := "abc"
	str2 := "cba"

	isPem(str1, str2)	
}