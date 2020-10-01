class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None

    # values are added in the begining
    def push(self, data):
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node

    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return

        while temp.next:
            # if current node and next node is same then delete next node
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new

            else:
                temp = temp.next

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__': 
  
    ll = LinkedList() 
    ll.push(1) 
    ll.push(2) 
    ll.push(2)
    ll.push(2)
    ll.push(3)
    ll.push(3)
    ll.push(4) 
    ll.printLL() 
    ll.removeDuplicates()
    ll.printLL()