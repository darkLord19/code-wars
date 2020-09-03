package main

import "fmt"

func binarySearch(arr []int, left int, right int, key int) int {
	for left <= right {
		mid := (left + right) / 2
		if key == arr[mid] {
			return mid
		} else if key < arr[mid] {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return -1
}

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

// duplicates are not handled in this approach
// Time Complexity: O(logn)
func search(arr []int, key int) int {
	pivot := -1
	pivot = findPivot(arr)
	if pivot == -1 {
		return binarySearch(arr, 0, len(arr)-1, key)
	}
	if arr[pivot] == key {
		return pivot
	}
	if arr[0] > key {
		return binarySearch(arr, pivot+1, len(arr)-1, key)
	}
	return binarySearch(arr, 0, pivot, key)
}

func main() {
	arr := []int{4, 5, 6, 7, 8, 9, 10, 1, 2, 3}
	fmt.Println(search(arr, 5))
	fmt.Println(search(arr, 7))
	fmt.Println(search(arr, 1))
}
