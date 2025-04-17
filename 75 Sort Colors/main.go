package main

import "fmt"

func sortColors(nums []int) []int  {

	var sorted []int

	const RED = 0
	const WHITE = 1
	const BLUE = 2

	ri, wi, bi := 0, 0, 0

	insert := func(slice []int, index, value int) []int {
		if index < 0 || index > len(slice){
			return slice
		} else {
			slice = append(slice[:index], append([]int{value},slice[index:]...)...)
		}

		return slice
	}

	for _, color := range nums {

		switch color{
		case RED:

			sorted = insert(sorted,ri,RED)
			ri += 1


		case WHITE:
			sorted = insert(sorted,wi,WHITE)
			wi = wi + ri + 1

		case BLUE:
			sorted = insert(sorted,bi,BLUE)
			bi = wi + ri + bi + 1


		}

		fmt.Println(sorted)
	}

	return sorted
	
	
}

func main() {

	nums := []int{2,0,2,1,1,0}

	fmt.Println(sortColors(nums))



}