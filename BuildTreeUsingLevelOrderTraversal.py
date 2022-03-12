from BinaryTree import Node

def buildTree():
    p = int( input())
    queue = []
    s = Node(p)
    queue.append( s)
    while bool( queue):
        n = queue.pop(0)
        c1 = int( input())
        c2 = int( input())
        if c1 != -1:
            m = Node( c1)
            n.left = s
            queue.append( s)
        if c2 != -1:
            k = Node( c2)
            n.right = k
            queue.append( k)
    return s

def printInorder(root):
    if root:
        printInorder(root.left)

        print(root.val),

        printInorder(root.right)

print( buildTree().val)

# 2 7 6 7 8 5 6 -1 -1 -1 -1 -1 -1 -1 -1
