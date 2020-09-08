# print middle of list


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
def middleOfList(li):
    first = li.head
    second = first.next
    while second != None:
        first = first.next
        if second.next != None:
            second = second.next.next
        else:
            break
    print(first.data)


if __name__ == "__main__":
    l = List()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(4)
    l.add(9)
    l.print()
    middleOfList(l)
