class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None

    # values are added in the beginned
    def push(self, data):
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node

    def reverse(self):
        prev = None
        current = self.head

        while current :
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        self.head = prev

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__': 
  
    ll = LinkedList() 
    ll.push(1) 
    ll.push(2); 
    ll.push(3); 
    ll.push(4) 
    ll.printLL() 
    ll.reverse()
    ll.printLL()