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

    def detectLoop(self):
        #floyed's algorithm
        slowp = self.head
        fastp = self.head
        while slowp and fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next

            if slowp == fastp:
                return slowp

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__': 
  
    ll = LinkedList() 
    ll.push(1) 
    ll.push(2)
    ll.push(3)
    ll.push(4) 
    ll.head.next.next.next = ll.head
    if ll.detectLoop():
        print("yes")
    else:
        print("no")