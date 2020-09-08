# check if loop exist in given linked list


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


# T(n): O(n)
# Space: O(n)
def detectLoop(li):
    visited = {}
    tmp = li.head
    while tmp != None:
        if tmp in visited:
            return True
        visited[tmp] = True
        tmp = tmp.next
    return False


# Floy'd slow and fast approach
# O(n) and no extra space
def detectLoopOptimized(li):
    slow = l.head
    fast = l.head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# 3rd method witn O(n) and constant space is to make next of each list point to tmp node
# if we come across a node which points to tmp then there is a loop

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
    print(detectLoopOptimized(l))
    l.head.next.next.next.next.next.next = l.head
    print(detectLoopOptimized(l))
