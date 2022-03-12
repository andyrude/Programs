from BinaryTree import Node

def flipEquiTrees( node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            noFlip = (node1.left, node2.right) and (node1.right, node2.left)
            flip = ( node1.left, node2.left) and ( node1.right , node2.right)
            return bool(flip or noFlip)

root1 = Node(10)
root1.left = Node(15)
root1.right = Node(16)
root1.left.left = Node(30)
root1.left.right = Node(45)
root1.right.left = Node(46)
root1.right.right = Node(79)
root2 = Node(10)
root2.left = Node(15)
root2.right = Node(16)
root2.left.left = Node(30)
root2.left.right = Node(45)
root2.right.left = Node(46)
root2.right.right = Node(79)
print( flipEquiTrees( root1, root2))
