package main

import "fmt"

// pick up an element and add in sorted portion of array
// sorted array is stored from start of the array
// Time complexity: O(n^2)
// max time taken if array is inversely sorted
// In place
// Stable
func insertionSort(arr []int) {
	l := len(arr)
	for i := 1; i < l; i++ {
		x := arr[i]
		j := i - 1
		for j >= 0 && arr[j] > x {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = x
	}
}

func main() {
	arr := []int{123, -123, 2122, 14, 5, 954, -145, 9, 0, 233, 123, 9}
	insertionSort(arr)
	fmt.Println(arr)
}
