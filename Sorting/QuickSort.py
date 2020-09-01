def partition(arr, left, right):
    i = left-1
    pivot = arr[right]

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return (i+1)


def quickSort(arr, left, right):
    if(left < right):
        p = partition(arr, left, right)

        quickSort(arr, left, p-1)
        quickSort(arr, p+1, right)


arr = [10, 8, 5, 6, 2, 4, 1, 3]
quickSort(arr, 0, 7)
for i in range(len(arr)):
    print(arr[i])