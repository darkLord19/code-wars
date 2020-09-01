def mergeSort(arr):
    if(len(arr) > 1):
        mid = len(arr)//2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        i, j, k = 0, 0, 0

        while(i < len(leftArr) and j < len(rightArr)):
            if(leftArr[i] < rightArr[j]):
                arr[k] = leftArr[i]
                i+=1
            else:
                arr[k] = rightArr[j]
                j+=1
             
            k+=1

        while(i<len(leftArr)):
            arr[k] = leftArr[i]
            k+=1
            i+=1
        while(j<len(rightArr)):
            arr[k] = rightArr[j]
            k+=1
            j+=1

arr = [10, 8, 5, 6, 2, 4, 1, 3]
mergeSort(arr)
for i in range(len(arr)):
    print(arr[i])