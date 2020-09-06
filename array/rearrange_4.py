# Given an array of random numbers,
# Push all the zero’s of a given array to the end of the array.

# Time: O(n)
# Space: O(1)
def rearrange(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1


if __name__ == "__main__":
    arr = list(map(int, input().split(" ")))
    rearrange(arr)
    print(arr)
