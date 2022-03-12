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


