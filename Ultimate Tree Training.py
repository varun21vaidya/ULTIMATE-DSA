# Tree Template for Python


# class Node():
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# def print2DUtil(root, space):

#     COUNT = 4
#     # Base case
#     if (root == None):
#         return

#     # Increase distance between levels
#     space += COUNT

#     # Process right child first
#     print2DUtil(root.right, space)

#     # Print current node after space
#     # count
#     print()
#     for i in range(COUNT, space):
#         print(end=" ")
#     print(root.value)

#     # Process left child
#     print2DUtil(root.left, space)

# # Wrapper over print2DUtil()


# def print2D(root):

#     # Pass initial space count as 0
#     print2DUtil(root, 0)


# # contruction of tree

# node = Node(1)
# node.left = Node(2)
# node.left.left = Node(4)
# node.left.right = Node(5)
# node.left.right.left = Node(8)
# node.right = Node(3)
# node.right.left = Node(6)
# node.right.right = Node(7)
# node.right.right.left = Node(9)
# node.right.right.right = Node(10)

# # Show Tree In Console
# print2D(node)


##################################################################


# # Traversals:

# # TC: O(n) n=number of nodes
# # SC: O(h) h=height of tree


# # Inorder Traversal: left root right

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.value, end=" ")
#         inorder(root.right)

# print("inorder")
# inorder(node)

# # ///////////////////////////////////////////////

# # # Preorder Traversal: root left right

# def preorder(root):
#     if root:
#         print(root.value, end=" ")
#         preorder(root.left)
#         preorder(root.right)

# print("preorder")
# preorder(node)

# # //////////////////////////////////////////////////

# # # Post Order Traversal: left right root

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.value, end=" ")

# print("postorder")
# postorder(node)
# print()

# # //////////////////////////////////////////////////


# # # BFS: Level Order Traversal

# # explanation:
# # store all the levels in each list
# # to do that we will store nodes in the queue
# # first we will store root in the queue then
# # pop that root, and then check if it has left and right
# # then add those child nodes in queue
# # and then insert that root in the level list
# # after inserting all nodes of that level
# # insert that level in the final ans list

# from collections import deque

# def BFS(root):
#     ans = []
#     if not root:
#         return ans
#     q = deque([root])

#     while q:
#         level = []
#         n = len(q)
#         for i in range(n):
#             currnode = q.popleft()
#             if currnode.left:
#                 q.append(currnode.left)
#             if currnode.right:
#                 q.append(currnode.right)
#             level.append(currnode.value)
#         ans.append(level)

#     print(ans)
#     return


# print("BFS Traversal")
# BFS(node)
