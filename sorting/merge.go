package main

import "fmt"

// merge left and right half of array in sorted order
func merge(arr []int, start int, mid int, end int) {
	tmp := make([]int, end-start+1)
	x, y, z := start, mid+1, 0
	for i := start; i <= end; i++ {
		if x > mid {
			tmp[z] = arr[y]
			z++
			y++
		} else if y > end {
			tmp[z] = arr[x]
			x++
			z++
		} else if arr[x] < arr[y] {
			tmp[z] = arr[x]
			z++
			x++
		} else {
			tmp[z] = arr[y]
			z++
			y++
		}
	}
	for i := 0; i < z; i++ {
		arr[start] = tmp[i]
		start++
	}
}

// Divide array in half recursively until there is only one member left
// then work your way upwards by merging left and right half of array
// Best Case Complexity: O(n*log n)
// Worst Case Complexity: O(n*log n)
// Average Case Complexity: O(n*log n)
// Space Complexity: O(n)
func mergeSort(arr []int, start int, end int) {
	if start < end {
		mid := (start + end) / 2
		mergeSort(arr, start, mid)
		mergeSort(arr, mid+1, end)
		merge(arr, start, mid, end)
	}
}

func main() {
	arr := []int{23, 331, -123, 23, -1, 28122, 84, 90, 0, 1}
	mergeSort(arr, 0, len(arr)-1)
	fmt.Println(arr)
}
