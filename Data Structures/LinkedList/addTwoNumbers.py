class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None

    def push(self, data):
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node

    def append(self, data):
        temp_node = Node(data)
        if self.head is None:
            self.head = temp_node
            return 
        current = self.head
        while current:
            current = current.next
        
        current = temp_node

    def addTwoLists(self, first, second):
        res = None
        temp = None
        prev = None
        carry = 0
        sum = 0

        while first or second:
            sum = carry + (first.data if first else 0) + (second.data if second else 0)
            carry = 1 if sum>=10 else 0
            sum = sum % 10

            temp = Node(sum)
            if res is None:
                res = temp
            else:
                prev.next = temp

            prev = temp
            if first:
                first = first.next
            if second:
                second = second.next
        
        if carry > 0:
            temp.next = None(carry)
            return res
