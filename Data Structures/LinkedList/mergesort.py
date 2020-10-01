class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None

    def append(self, data):
        temp_node = Node(data)
        if self.head is None:
            self.head = temp_node
            return 
        current = self.head
        while current:
            current = current.next
        
        current = temp_node

    def merge(self, left, right):
        result = None
        if left is None:
            return right
        if right is None:
            return left

        if left.data<=right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result

    def merge_inplace(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        if left.data<= right.data:
            left.next = self.merge_inplace(left.next, right)
            return left
        else:
            right.next = self.merge_inplace(left, right.next)
            return right

    def mergesort(self, head):
        if head is None:
            return head

        middle = self.getMiddle(head)
        nextToMiddle = middle.next

        middle.next = None

        left = self.mergesort(head)
        right = self.mergesort(nextToMiddle)

        sortedList = self.merge(left, right)
        return sortedList
    
    def getMiddle(self, head):
        if head is None:
            return head

        slowptr = head
        fastptr = head

        while fastptr and fastptr.next:
            fastptr = fastptr.next.next
            slowptr = slowptr.next

        return slowptr
