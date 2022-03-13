from ll import Node
def middlNode( node):
    fast = node
    slow = node
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    if fast.next is not None:
        return slow.next
    return slow
