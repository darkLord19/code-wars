class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class  LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def rotate(self, k):
        if(k == 0):
            return
        current = self.head
        count = 1
        while count < k and current is not None:
            current = current.next
            count += 1
        if current is None:
            return

        kthNode = current

        while current.next is not None:
            current = current.next

        current.next = self.head
        self.head = kthNode.next
        kthNode.next = None

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1,9):
        ll.push(i)
    ll.printLL()
    ll.rotate(3)
    ll.printLL()