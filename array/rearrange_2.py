# Given an array of n elements. Our task is to write a program
# to rearrange the array such that elements at even positions
# are greater than all elements before it and elements at
# odd positions are less than all elements before it.

# Time Complexity: O(logn)
# Space: O(n)
# sort the array in increasing order and in new array
# add from the smallest value from the end of the indices on odd positions
# i.e. 1 2 3 4 5 6 7
# -> x x x x x x 1
# -> x x x x 2 x 1
# -> x x 3 x 2 x 1
# -> 4 x 3 x 2 x 1
# then add for even positions from the start
# -> 4 5 3 x 2 x 1
# -> 4 5 3 6 2 x 1
# -> 4 5 3 6 2 7 1
def rearrange(arr):
    tmp = sorted(arr)
    even = int(len(arr) / 2)
    odd = len(arr) - even
    j = odd - 1
    for i in range(0, len(arr), 2):
        arr[i] = tmp[j]
        j -= 1
    j = odd
    for i in range(1, len(arr), 2):
        arr[i] = tmp[j]
        j += 1


if __name__ == "__main__":
    arr = list(map(int, input().split(" ")))
    rearrange(arr)
    print(arr)
