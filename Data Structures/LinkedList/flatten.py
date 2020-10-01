class Node:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.next = None
        self.bottom = None

class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None

    # def append(self, data):
    #     temp_node = Node(data)
    #     if self.head is None:
    #         self.head = temp_node
    #         return 
    #     current = self.head
    #     while current:
    #         current = current.next
        
    #     current = temp_node
    
    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        result = None
        if left.data <= right.data:
            result = left
            result.bottom = self.merge(left.bottom, right)
        else:
            result = right
            result.bottom = self.merge(left, right.bottom)

        result.next = None
        return result

    def flatten(self, head):
        if head is None or head.next is None:
            return head
        next = self.flatten(head.next)
        return self.merge(head, next)