# An array contains both positive and negative numbers in random order.
# Rearrange the array elements so that positive and negative numbers
# are placed alternatively. Number of positive and negative numbers
# need not be equal. If there are more positive numbers they
# appear at the end of the array. If there are more negative numbers,
# they too appear in the end of the array.

# O(n)
def rearrange(arr):
    pivot = 0
    j = -1
    # partition array in two parts
    for i in range(0, len(arr)):
        if arr[i] < pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    pos, neg = j + 1, 0
    tmp = []
    # rotate array by d(diff between negitive and positive numbers)
    if pos > len(arr) - pos:
        d = pos - (len(arr) - pos)
        tmp = arr[:d][::-1] + arr[d:][::-1]
        tmp = tmp[::-1]
        pos = int((len(arr) - d) / 2)
        n = len(arr) - d

    # swap every alternate negative number with next
    # positive number
    while pos < n and neg < pos and tmp[neg] < 0:
        tmp[pos], tmp[neg] = tmp[neg], tmp[pos]
        pos += 1
        neg += 2

    return tmp


if __name__ == "__main__":
    arr = list(map(int, input().split(" ")))
    arr = rearrange(arr)
    print(arr)
