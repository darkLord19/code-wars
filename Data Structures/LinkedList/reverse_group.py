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

    def reverse_util(self, head, k):
        if head is None:
            return
        current = head
        prev = None
        next = None
        count = 0

        while count < k and current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.rotate_util(next, k)

        return prev

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverse(self, k):
        if k == 0:
            return
        self.head = self.rotate_util(self.head, k)

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1,10):
        ll.push(i)
    ll.printLL()
    ll.reverse(3)
    ll.printLL()