def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def leftRotate(arr, d, n):
    d = d % n
    _gcd = gcd(d, n)
    for i in range(_gcd):
        temp = arr[i]
        j=i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def printArray(arr, n): 
    for i in range(n): 
        print (arr[i]) 


arr = [1, 8, 9, 2, 4, 3, 6] 
n = len(arr) 
d = 3
leftRotate(arr, d, n) 
printArray(arr, n) 