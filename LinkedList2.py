from ll import Node
from ll import LinkedList
def middlNode( node):
    fast = node
    slow = node
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    if fast.next is not None:
        return slow.next
    return slow

def mergeTwoSortedLists( node1, node2):
    dummyNode = Node(-1)
    head = Node()
    dummyNode.next = head
    if node1.data <= node2.data:
        head.data = node1.data
        node1.head = node1.next
    else:
        head.data = node2.data
        node2.head = node1.next
    while node1.head is not None or node2 is not None:
        if node1.data <= node2.data:
            head.next = Node( node1.data)
            node1 = node1.next
        else:
            head.next = Node( node2.data)
            node2 = node2.next
        head = head.next
    if node1 is None:
        head.next = node2
    else:
        head.next = node1
    return dummyNode.next
