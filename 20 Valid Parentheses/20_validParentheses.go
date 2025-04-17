package main

import "fmt"

func isValid(s string) bool {

	// declare empty stack
	var stack []rune

	var parentheses = map[rune]rune{')':'(', ']':'[', '}':'{'}

	for _, value := range s{
		
		// if is closing parenthesis
		if opening, found := parentheses[value]; found{

			if len(stack) == 0 || stack[len(stack)-1] != opening{
				return false
			}

			// remove from stack
			stack = stack[:len(stack)-1]
		} else {

			stack = append(stack,value)

		}

	}

	return len(stack) == 0
    
}

func main() {

	s := "(]"
	fmt.Println(isValid(s))

}