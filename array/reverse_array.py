# Write a program to reverse an array or string

# O(n)
def reverse(arr):
    l = 0
    r = len(arr) - 1
    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1


if __name__ == "__main__":
    arr = list(map(int, input().split(" ")))
    reverse(arr)
    print(arr)
