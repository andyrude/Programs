from ll import LinkedList
from ll import Node
def secondMiddl( head):
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    print( slow.data)

def duplicateData( head):
    current = head
    dummyNode = Node(-1)
    dummyNode.next = current
    while current.next is not None:
        if current.data == current.next.data:
            temp = current.next.next
            current.next = temp
    return dummyNode.next

def display( head):
    node = head
    while node is not None:
        print( node.data)
        node = node.next





l1 = LinkedList()
l1.head = Node(20)
l1.head.next = Node(30)
l1.head.next.next = Node(30)
l1.head.next.next.next = Node( 70)
l1.head.next.next.next.next = Node(130)
l1.head.next.next.next.next.next = Node(130)
display(duplicateData( l1.head))
