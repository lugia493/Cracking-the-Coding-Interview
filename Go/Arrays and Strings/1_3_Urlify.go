package main

import "fmt"

func urlify(str string) string { 
	url := "%20"
	str_url := ""

	for _, v := range str {
		if string(v) == " " {
			str_url += url
		} else {
			str_url += string(v)
		}
	}
	return str_url
}

func main() {
	str := "Hello World, I am Daniel Ramsey    "
	fmt.Println(urlify(str))
}