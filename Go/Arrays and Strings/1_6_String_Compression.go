package main 

import (
	"fmt"
	"strconv"
)

func SC (str string) string {

	str_comp := ""
	count := 0

	for i := 0; i < len(str); i++ {
		count++
		if i + 1 >= len(str) || string(str[i]) != string(str[i + 1]) {
				str_comp += string(str[i]) + strconv.Itoa(count)
				count = 0
		}	
	}

	if len(str_comp) > len(str) {
		return str
	} else {
		return str_comp
	}
}

func main() {
	str := "aaabbbcccd"
	fmt.Println(SC(str))
}