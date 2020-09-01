package main

import "fmt"

// Iterate over whole array and swap adjacent elements
// if they are in wrong order
// Time complexity: O(n^2)
// Space complexity: O(1)
// Stabel sort: true
func bubbleSort(arr []int) {
	l := len(arr)
	for i := 0; i < l-1; i++ {
		for j := 0; j < l-1-i; j++ {
			if arr[j] > arr[j+1] {
				tmp := arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = tmp
			}
		}
	}
}

// if inner loop doesn't swap any elements then stop
// as array is already sorted
// best case complexity: O(n)
// worst case complexity: O(n^2)
// Space complexity
func bubbleSortOptimized(arr []int) {
	l := len(arr)
	swapped := false
	for i := 0; i < l-1; i++ {
		swapped = false
		for j := 0; j < l-i-1; j++ {
			if arr[j] > arr[j+1] {
				tmp := arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = tmp
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}
}

// keep track of last swapped index and loop till that only
func bubbleSortOptimizedTwo(arr []int) {
	l := len(arr)
	for l >= 1 {
		newl := 0
		for i := 0; i < l-1; i++ {
			if arr[i] > arr[i+1] {
				tmp := arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = tmp
				newl = i + 1
			}
		}
		l = newl
	}
}

func main() {
	arr := []int{10, -9, 12, 3, -11, 0, 100, 122, -104}
	arr2 := []int{123, -2893, 12, 24, -812, 23, -8, 9, 0, 1}
	arr3 := []int{12, 1232, 1123, -1231, 1232, 10123, 12212, 12, -123, 1, -12, 12, -1}
	bubbleSort(arr)
	fmt.Println(arr)
	bubbleSortOptimized(arr2)
	fmt.Println(arr2)
	bubbleSortOptimizedTwo(arr3)
	fmt.Println(arr3)
}
