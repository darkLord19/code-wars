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

    # values are added in the end
    def append(self, data):
        temp_node = Node(data)
        if self.head is None:
            self.head = temp_node
            return

        # get last node
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = temp_node

    def printLL(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__': 
  
    ll = LinkedList() 
    ll.append(1) 
    ll.push(2); 
    ll.push(3); 
    ll.append(4) 
    ll.printLL() 