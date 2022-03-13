from BinaryTree import Node
from TryFunctions import height
def SymmetricTree( node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is not None and node2 is not None:
        if node1.val == node2.val:
            return SymmetricTree( node1.left, node2.right) and SymmetricTree( node1.right, node2.left)
    return False

def Dia( node):
    if node is None:
        return 0
    c1 = height( node.left)
    c2 = height( node.right)
    getDia = c1 + c2 + 2
    return max( getDia, max( c1, c2))

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
root2 = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(4)
print( SymmetricTree( root, root2))
print( Dia( root))