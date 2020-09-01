package main

import "fmt"

func binarySearch(arr []int, key int) bool {
	left := 0
	right := len(arr) - 1

	for left <= right {
		mid := (left + right) / 2
		if key == arr[mid] {
			return true
		} else if key < arr[mid] {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return false
}

func main() {
	arr := []int{1, 2, 3, 4, 6, 9, 10}
	fmt.Println(binarySearch(arr, 4))
	fmt.Println(binarySearch(arr, 11))
}
