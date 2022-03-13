from ll import LinkedList
from ll import Node
def secondMiddl( head):
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    print( slow.data)


l1 = LinkedList()
l1.head = Node(20)
l1.head.next = Node(30)
l1.head.next.next = Node(40)
l1.head.next.next.next = Node( 70)
l1.head.next.next.next.next = Node(130)
l1.head.next.next.next.next.next = Node(130)
secondMiddl( l1.head)