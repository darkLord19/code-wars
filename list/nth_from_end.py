# Program for n’th node from the end of a Singly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def add(self, data):
        tmp = Node(data)
        last = self.head

        if self.head == None:
            self.head = tmp
            return

        while last.next != None:
            last = last.next

        last.next = tmp

    def print(self):
        last = self.head
        while last != None:
            print(last.data, end=" ")
            last = last.next
        print()


# O(n)
def nthFromEnd(li, n):
    first = li.head
    for i in range(n):
        if first == None:
            print("n is greater than size of list")
            return
        first = first.next
    second = li.head
    while first != None:
        first = first.next
        second = second.next
    print(second.data)


if __name__ == "__main__":
    l = List()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.print()
    nthFromEnd(l, 1)
