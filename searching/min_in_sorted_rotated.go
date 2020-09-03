//Find the minimum element in a sorted and rotated array

package main

import "fmt"

// search pivot element doing modified binary search
func findPivot(arr []int) int {
	l := 0
	r := len(arr) - 1
	for l <= r {
		mid := (l + r) / 2
		if arr[mid] > arr[mid+1] && mid < r {
			return mid
		}
		if arr[mid-1] > arr[mid] && mid > l {
			return mid - 1
		}
		if arr[l] >= arr[mid] {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	return -1
}

// find pivot element. next of pivot is min
// without considering duplicates
func min(arr []int) int {
	pivot := -1
	pivot = findPivot(arr)
	return arr[pivot+1]
}

func main() {
	arr := []int{4, 5, 6, 7, 8, 9, 10, 1, 2, 3}
	fmt.Println(min(arr))
	arr = []int{4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3}
	fmt.Println(min(arr))
}
