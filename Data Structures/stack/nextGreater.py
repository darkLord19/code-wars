class Stack:
    def __init__(self):
        self.s = []
    def isEmpty(self):
        return len(self.s) == 0

    def push(self, k):
        self.s.append(k)

    def pop(self):
        if not self.isEmpty():
            return self.s.pop()

def printNGE(arr):
    s = Stack()
    next = 0
    element = 0

    s.push(arr[0])

    for i in range(1, len(arr)):
        next = arr[i]

        if not s.isEmpty():
            element = s.pop()

            while element < next:
                print(element, next)
                if s.isEmpty():
                    break
                element = s.pop()

            if element > next:
                s.push(element)

        s.push(next)

    while not s.isEmpty():
        element = s.pop() 
        next = -1
        print(str(element) + " -- " + str(next)) 

def nextNGEInOrder(arr):
    s = list()
    n = len(arr)
    arr1 = [0 for i in range(len(n))] 
    for i in range(n-1, -1, -1):

        # compare current element with the top of the stack
        # while current element is greater than top, keep 
        # popping it
        while len(s) > 0 and s[-1]<=arr[i]:
            s.pop()
        # if stack is empty then it means there's no element
        # on the right which is greater than the current element
        if len(s) == 0:
            arr1[i] = -1
        # if stack is not empty then it means there's an element
        # in the stack which is grater than the current element
        else:
            arr1[i] = s[-1]
        s.append(arr[i])
arr = [11, 13, 21, 3] 
printNGE(arr) 