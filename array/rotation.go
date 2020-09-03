// Write a function rotate(ar[], d, n) that rotates
// arr[] of size n by d elements.

package main

import "fmt"

// Time Complexity: O(n)
// Space Complexity: O(d)
func rotateBruteForce(arr []int, d int, n int) {
	tmp := make([]int, d)
	for i := 0; i < d; i++ {
		tmp[i] = arr[i]
	}
	j := 0
	for i := d; i < n; i++ {
		arr[j] = arr[i]
		j++
	}
	j = 0
	for i := n - d; i < n; i++ {
		arr[i] = tmp[j]
		j++
	}
}

// Time Complexity: O(n*d)
// Space Complexity: O(1)
func rotate(arr []int, d int, n int) {
	for i := 0; i < d; i++ {
		tmp := arr[0]
		for j := 1; j < n; j++ {
			arr[j-1] = arr[j]
		}
		arr[n-1] = tmp
	}
}

func reverse(arr []int, l int, r int) {
	for l < r {
		arr[l], arr[r] = arr[r], arr[l]
		l++
		r--
	}
}

// Time Complexity: O(n)
func rotateReverse(arr []int, d int, n int) {
	reverse(arr, 0, d-1)
	reverse(arr, d, n-1)
	reverse(arr, 0, n-1)
}

func main() {
	arr := []int{1, 2, 4, 5, 6, 12, 23, 44, 55, 62, 6, 112}
	rotateBruteForce(arr, 3, len(arr))
	fmt.Println(arr)
	rotate(arr, 3, len(arr))
	fmt.Println(arr)
	rotateReverse(arr, 2, len(arr))
	fmt.Println(arr)
}
