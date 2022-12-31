# Tree Template for Python

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print2DUtil(root, space):

    COUNT = 4
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT, space):
        print(end=" ")
    print(root.value)

    # Process left child
    print2DUtil(root.left, space)

# Wrapper over print2DUtil()


def print2D(root):

    # Pass initial space count as 0
    print2DUtil(root, 0)



node=Node(1)
node.left=Node(2)
node.left.left=Node(4)
node.left.right=Node(5)
node.left.right.left=Node(8)
node.right=Node(3)
node.right.left=Node(6)
node.right.right=Node(7)
node.right.right.left=Node(9)
node.right.right.right=Node(10)
print2D(node)