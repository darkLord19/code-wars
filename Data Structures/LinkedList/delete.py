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

    def delete(self, pos):
        if self.head is None:
            return

        temp = self.head
            
        if pos == 0:
            self.head = temp.next
            temp = None
            return

        # find previous node of the node that you want to delete
        for i in range(pos-1):
            temp = temp.next
            # if position > length of linked list then break
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return 
        
        next = temp.next.next
        temp.next = None
        temp.next = next

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
    ll.delete(2)
    ll.printLL() 