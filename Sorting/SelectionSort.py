def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [10, 8, 5, 6, 2, 4, 1, 3]
selectionSort(arr)
for i in range(len(arr)):
    print(arr[i])