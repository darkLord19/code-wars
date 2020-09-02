// Given an array of integers.
// All numbers occur twice except one number which occurs once.
// Find the number in O(n) time & constant extra space.

package main

import "fmt"

func main() {
	arr := []int{2, 2, 3, 4, 1, 1, 4, 3, 5, 5, 7}

	ans := 0

	// Xor all the elements.
	// Xor of same int is 0 i.e. 1 XOR 1 = 0
	// so all same numbers will cancel out eachother
	for _, x := range arr {
		ans ^= x
	}

	fmt.Println(ans)

	// Other approach is to use hashtable

}
