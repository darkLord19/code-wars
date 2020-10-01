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

    def isPalindrome(self):
        slowp = self.head
        fastp = self.head
        prev_of_slow_ptr = self.head

        mid = None
        second_head = None
        res = True

        if self.head and self.head.next :

            # find mid node
            while fastp and fastp.next:
                fastp = fastp.next.next
                prev_of_slow_ptr = slowp
                slowp = slowp.next

            # if number of elements are odd, skip the middle node 
            # and store it in mid to use it later
            if fastp:
                mid = slowp
                slowp = slowp.next

            # reverse the second half and compare it with the first half
            second_head = slowp
            prev_of_slow_ptr.next = None # detach from second ll's head
            second_head = self.reverse(second_head)
            res = self.compareLL(self.head, second_head)

            # set LL as it was
            second_head = self.reverse(second_head)
            if mid:
                prev_of_slow_ptr.next = mid
                mid.next = second_head
            else:
                prev_of_slow_ptr.next = second_head

            return res


    def compareLL(self, head1, head2):
        temp1 = head1
        temp2 = head2
        while temp1 and temp2:
            if temp1.data == temp2.data:
                temp1 = temp1.next
                temp2 = temp2.next

            else:
                return False
        
        if temp1 is None and temp2 is None:
            return True
        
        return False

    def reverse(self, second_head):
        prev = None
        current = second_head

        while current :
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        second_head = prev
        return second_head


    def printLL(self, head):
        temp = head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=='__main__': 
  
    ll = LinkedList() 
    # ll.push(1) 
    ll.push(2); 
    ll.push(3)
    ll.push(4)
    ll.push(3)
    ll.push(2)
    ll.push(1)
    print(ll.isPalindrome()) 
    # ll.printLL(ll.head) 