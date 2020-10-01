class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node
    
    def printLL(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data)
            temp_node = temp_node.next

    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        print(slow_ptr.data)

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1,9):
        ll.push(i)

    ll.printLL()
    ll.printMiddle()