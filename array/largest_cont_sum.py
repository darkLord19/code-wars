# Write an efficient program to find the sum of
# contiguous subarray within a one-dimensional array of
# numbers which has the largest sum.

# kadane's algorithm
def largest_cont_sum(arr):
    max_sum = arr[0]
    curr_max = arr[0]
    start = 0
    end = 0
    s = 0
    for i in range(1, len(arr)):
        curr_max += arr[i]
        if curr_max > max_sum:
            max_sum = curr_max
            start = s
            end = i
        if curr_max < 0:
            curr_max = 0
            s = i + 1
    return max_sum, start, end


if __name__ == "__main__":
    arr = list(map(int, input().split(" ")))
    msum, start, end = largest_cont_sum(arr)
    print(msum, start, end)
