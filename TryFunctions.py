from BinaryTree import Node
def FlipEquivalent( node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    noFlip = FlipEquivalent( node1.left, node2.left) and FlipEquivalent( node1, node2.right)
    flip = FlipEquivalent( node1.left, node2.right) and FlipEquivalent( node1.right, node2.left)
    return noFlip or flip


max_depth = -1
def RightSideView( node, current_lev):
    global max_depth
    if node is None:
        return
    if max_depth < current_lev:
        print( node.val)
        max_depth = current_lev
    RightSideView( node.right, current_lev + 1)
    RightSideView( node.left, current_lev  +1)

def LeftSideView( node, current_lev):
    global max_depth
    if node is None:
        return
    if max_depth < current_lev:
        print( node.val)
        max_depth = current_lev
    LeftSideView( node.left, current_lev)
    LeftSideView( node.right, current_lev)

def inOrderT( node):
    if node is None:
        return None
    inOrderT( node.left)
    print( node.val)
    inOrderT( node.right)

def postOrder( node):
    if node  is None:
        return None
    postOrder( node.left)
    postOrder( node.right)
    print( node.val)

def preOrder( node):
    if node is None:
        return None
    print( node.val)
    preOrder( node.left)
    preOrder( node.right)

def height( node):
    if node is None:
        return -1
    c1 = height( node.left)
    c2 = height( node.right)
    return max( c1, c2) + 1

def dia( node):
    if Node is None:
        return 0
    c1 = height( node.left)
    c2 = height( node.right)
    return max( c1+c2 + 2, max( c1, c2))



