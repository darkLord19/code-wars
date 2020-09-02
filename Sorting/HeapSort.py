def heapify(arr, n, root):
    largest = root
    l = 2 * root + 1
    r = 2 * root + 2

    if l < n and arr[root] < arr[l]:
        largest = l

    if r < n and arr[root] < arr[r]:
        largest = r
    
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        # Heapify for root i
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # arr[0] is the highest
        # swap it with the ith and heapify the rest
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [10, 8, 5, 6, 2, 4, 1, 3]
heapSort(arr)
for i in range(len(arr)):
    print(arr[i])