package main

import (
	"fmt"
	"slices"
)

// 1. Sort the Array: Begin by sorting the array. This helps in efficiently finding pairs and skipping duplicates.

// 2. Iterate with a Fixed Pointer: Fix one number at a time and use a two-pointer approach for the rest of the array.

// 3. Apply Two-pointer Technique: For each fixed number, initialize two pointers—one at the start
//    (right after the fixed pointer) and one at the end of the array. Move these pointers based on the sum comparison.

// 4. Check for Zero Sum: If the sum of the numbers at the two pointers with the fixed number is zero,
//    record the triplet.

// 5. Skip Duplicates: After finding a triplet or moving a pointer, always skip the duplicate numbers to avoid
//    duplicate triplets in the result.

func threeSum(nums []int) [][]int {

	// sorting nums
	slices.Sort(nums)

	// empty list
	results := [][]int{}

	for i := 0; i < len(nums) - 2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue // skip duplicate numbers
		}

		left, right := i + 1, len(nums)-1

		for left < right {
			current_sum := nums[i] + nums[left] + nums[right]

			if current_sum == 0 {
				results = append(results, []int{nums[i], nums[left], nums[right]})

				for left < right && nums[left] == nums[left + 1] {
					left +=1
				}
	
				for left < right && nums[right] == nums[right - 1] {
					right -=1
				}
	
				left += 1
				right -= 1
			} else if current_sum < 0 {
				left +=1
			} else {
				right -=1
			}

			
		}
	}
	return results

}

func main() {

	nums := []int{0,0,0}
	fmt.Println(threeSum(nums))

}