package main

import "fmt"

// In every iteration of selection sort, the minimum element (considering ascending order)
// from the unsorted subarray is picked and moved to the sorted subarray.
// Time complexity: O(n^2)
// Space: O(1)
// Unstable
func selectionSort(arr []int) {
	l := len(arr)
	for i := 0; i < l; i++ {
		minI := i
		for j := i; j < l; j++ {
			if arr[j] < arr[minI] {
				minI = j
			}
		}
		min := arr[minI]
		arr[minI] = arr[i]
		arr[i] = min
	}
}

func main() {
	arr := []int{123, -123, 2122, 14, 5, 954, -145, 9, 0, 233, 123, 9}
	selectionSort(arr)
	fmt.Println(arr)
}
