package main

import "fmt"

func plusOne(digits []int) []int {

	length := len(digits)
	carry := 1
	index := length - 1

	for carry == 1 && index >= 0 {

		if digits[index] + 1 > 9 {
			digits[index] = 0
			carry = 1
		} else {
			digits[index] = digits[index] + 1
			carry = 0
		}

		index -= 1
	}

	if carry == 1 {
		digits = append([]int{1},digits...)
	}

	return digits
}

func main() {
	digits := []int{9,9,9}

	fmt.Println(plusOne(digits))
}