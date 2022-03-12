from BinaryTree import Node
def levelOrderBt(node):
    queue = [ node]
    helper = []
    while bool( queue):
        rem = queue.pop( 0);
        print( rem.val , end = " ")
        if rem.left is not None:
            helper.append( rem.left)
        if rem.right is not None:
            helper.append( rem.right)
        if bool( queue) == False:
            queue = helper
            helper = []
            print()

root = Node(10)
root.left = Node(15)
root.right = Node(25)
root.left.left = Node(35)
root.left.right = Node(75)
root.right.left = Node(65)
root.right.right = Node(58)
root.left.right.left = Node(87)
levelOrderBt( root)
