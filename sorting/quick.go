package main

import "fmt"

func partition(arr []int, start int, end int) int {
	pivot := arr[end]
	j := start - 1
	for i := start; i < end; i++ {
		if arr[i] < pivot {
			j++
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	arr[j+1], arr[end] = arr[end], arr[j+1]
	return j + 1
}

func quickSort(arr []int, start int, end int) {
	if start < end {
		p := partition(arr, start, end)
		quickSort(arr, start, p-1)
		quickSort(arr, p+1, end)
	}
}

func main() {
	arr := []int{23, 331, -123, 23, -1, 28122, 84, 90, 0, 1}
	quickSort(arr, 0, len(arr)-1)
	fmt.Println(arr)
}
