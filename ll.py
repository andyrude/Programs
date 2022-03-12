class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end = " --> ")
            temp = temp.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__=='__main__':
        ll = LinkedList()
        ll.head = Node(15)
        ll.head.next = Node( 25)
        ll.head.next.next = Node(35)
        ll.printList()
