// Rearrange an array such that arr[i] = i

package main

import "fmt"

// Time complexity: O(n^2)
func rearrange(arr []int) {
	for i := range arr {
		if arr[i] == -1 || arr[i] == i {
			continue
		}
		j := arr[i]
		for arr[j] != j && arr[j] != -1 {
			tmp := arr[j]
			arr[j] = j
			j = tmp
		}
		arr[j] = j
		if arr[i] != i {
			arr[i] = -1
		}
	}
}

// O(n)
func rearrangeOptimized(arr []int) {
	for i := 0; i < len(arr); {
		if arr[i] > 0 && arr[i] != i {
			arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
		} else {
			i++
		}
	}
}

func main() {
	arr := []int{3, 1, 0, 2, -1}
	rearrange(arr)
	fmt.Println(arr)
	arr = []int{-1, 5, 3, 4, 1, 2}
	rearrangeOptimized(arr)
	fmt.Println(arr)
}
