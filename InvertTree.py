from BuildTreeUsingLevelOrderTraversal import buildTree
def invert_Tree( root):
    if root is None:
        return None
    left = invert_Tree( root.left)
    right = invert_Tree( root.right)
    root.right = left
    root.left = right
    return root


def printInorder(root):
    if root:
        printInorder(root.left)

        print(root.val),

        printInorder(root.right)


printInorder(invert_Tree( buildTree()))

# 2 7 6 7 8 5 6 -1 -1 -1 -1 -1 -1 -1 -1
