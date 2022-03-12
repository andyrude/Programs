from BinaryTree import Node

max_depth = -1
def rightSideView(node, curr_lev):
    if node is None:
        return
    global  max_depth
    if max_depth < curr_lev:
        print( node.val)
        max_depth = curr_lev
    rightSideView( node.right, curr_lev + 1)
    rightSideView( node.left, curr_lev + 1)

root1 = Node(10)
root1.left = Node(15)
root1.right = Node(16)
root1.left.left = Node(30)
root1.left.right = Node(45)
root1.right.left = Node(46)
root1.right.right = Node(79)
rightSideView( root1, 0)