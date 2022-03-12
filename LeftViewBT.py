from BinaryTree import Node
max_dep = -1
def leftViewBinaryTree( root, curr):
    global max_dep
    if root is None:
        return;
    global max_dep
    if max_dep < curr:
        print( root.val, end = " ")
        max_dep = curr
    leftViewBinaryTree( root.right, curr + 1)
    leftViewBinaryTree( root.left, curr + 1)

root = Node(10)
root.left = Node(15)
root.right = Node(65)
root.left.left = Node( 46)
root.right.left = Node(76)
leftViewBinaryTree( root, 0)