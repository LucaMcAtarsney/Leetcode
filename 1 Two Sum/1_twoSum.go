package main

import "fmt"

func twoSum(nums []int, target int) []int {
	
	numMap := make(map[int]int)

	for i, value := range nums {

		complement := target - value

		if index, found := numMap[complement]; found {

			return []int{index,i}
		}
		numMap[value] = i

	}

	return nil

}

func main() {

	nums := []int{1,2,3,4,5}
	var target int = 9

	fmt.Println(twoSum(nums,target))
}