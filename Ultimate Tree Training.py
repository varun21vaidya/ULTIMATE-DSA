# Tree Template for Python

# Tree Node
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ** To show tree in console use print2DUtil and print2D functions
# and call print2D with root as param in your code

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



# contruction of Example tree

node = Node(1)
node.left = Node(2)
node.left.left = Node(4)
node.left.right = Node(5)
node.left.right.left = Node(8)
node.right = Node(3)
node.right.left = Node(6)
node.right.right = Node(7)
node.right.right.left = Node(9)
node.right.right.right = Node(10)

# Show Tree In Console
print2D(node)


###########################  Traversals    #######################################

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

# # # /////////////////////////////////////////////////////////////////////


# # # Preorder Traversal: root left right

# def preorder(root):
#     if root:
#         print(root.value, end=" ")
#         preorder(root.left)
#         preorder(root.right)

# print("preorder")
# preorder(node)

# # # /////////////////////////////////////////////////////////////////////


# # # Post Order Traversal: left right root

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.value, end=" ")

# print("postorder")
# postorder(node)
# print()

# # # /////////////////////////////////////////////////////////////////////



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
#     return ans


# print("BFS Traversal")
# BFS(node)

# # # /////////////////////////////////////////////////////////////////////

# # # Iterative Preorder Traversal (root left right):

# # Explanation:
# # to move iteratively we need to store the root nodes somewhere
# # USE LILO ds ie stack to store left right nodes
# # Now as in preorder root left right, so when getting elements from stack
# # we will need left first then right, so insert right first then left
# # now suppose main root is inserted in stack, pop it and 
# # append right and then left nodes to stack, then pop next element ie left
# # and get its right and left nodes...
# # when popping store those elements in saperate list as preorder treaversal

# def iterative_preorder(root):
#     if not root:
#         return
#     stack=[root]
#     ans=[]
#     while stack:
#         currnode=stack.pop()
#         if currnode.right:
#             stack.append(currnode.right)
#         if currnode.left:
#             stack.append(currnode.left)
#         ans.append(currnode.value)

#     print(ans)
#     return ans

# print("iterative preorder")
# iterative_preorder(node)
# print()


# # # /////////////////////////////////////////////////////////////////

# # # Iterative Inorder (left root right)

# # Explanation:
# # to make inorder traversal, ie left root right
# # we need to traverse to extreme left and
# # then if there are no more nodes, append that node to result
# # and untill then we need to store previous nodes somewhere 
# # so we can use a LIFO ds ie stack which will pop recently added element
# # so first of all traverse to left and add nodes to stack until it becomes null
# # then when it becomes null pop out last added node in stack
# # and add that ele to result, and traverse to right of that stack
# # when a stack becomes empty return the result

# def iterative_inorder(root):
#     stack=[]
#     res=[] 
#     currnode=root
#     while True:
#         if currnode:
#             stack.append(currnode)
#             currnode=currnode.left
#         else: #currnode is null
#             if not stack: # stack is empty
#                 break
#             currnode=stack.pop()
#             res.append(currnode.value)
#             currnode=currnode.right
    
#     print(res)
#     return res

# print("iterative inorder")
# iterative_inorder(node)
# print()





# # # /////////////////////////////////////////////////////////////////

# # # Iterative Post Order (left root right)

# # Explanation: 2 Stacks
# to get postorder iteratively use 2 stacks
# one for taking the current node from tree
# then pop that node and add it to stack2
# and add left and right nodes to stack1
# now again get top element popped ie loop
# now when stack1 gets empty we have traversed all the tree nodes
# and those nodes are in stack2 in reverse order
# so pop out values from that stack2 and add to result array
def iterative_postorder(root):
    st1=[root]
    st2=[]
    res=[]
    while st1:
        curr=st1.pop()
        st2.append(curr)
        if curr.left: st1.append(curr.left)
        if curr.right: st1.append(curr.right)
    
    while st2:
        res.append(st2.pop().value)

    print(res)
    return res


print("iterative postorder")
iterative_postorder(node)
print()




# # Explanation: 1 Stacks
# now we have to solve this using only 1 stack
# to do this we need to traverse to extreme left,
# until its null, and post the curr value to stack
# now when we reach the null go to else condition 
# use temp to asign value at right side of top of the stack
# ie its parent nodes right side, 
# ie we have checked all left node now its time to move right side
# if right side has value, assign it to curr, so it can traverse to its left
# and add those values to stack, until it becomes null again
# but that temp ie parents right node has no value ie null
# then pop the last element of stack ie last node of tree we covered and not printed yet.
# and that is value we need to add to result 
# ie we have checked left then right now pop elements and get parent nodes
# then if that temp is part of right leaning subtree ie it is right side of its parent
# and if there is more such elements we can directly take all of them with a while loop
# so just check if temp is equal to top of stacks right element if it is
# then pop that top values and add it to result
# thats it, this whole code can cover if tree is going to left go to extreme left
# if found dead end, check parent nodes right subtree and make it current, ie go to that subtrees left then right
# now found dead end again? to right also ? pop from the stack which will be the values to be resulted
# if there is right leaning tree contineously pop elements and give result which will also include its parent nodes
def iterative_postorder(root):

    curr=root
    temp=None
    stack= []
    res=[]
    while True:

        # final condition, loop is not at beginnning 
        # and still stack become empty
        if curr!=root and not stack:
            print(res)
            return res

        # if curr has value, add it to stack, move to its left values
        if curr:
            stack.append(curr)
            curr=curr.left

        else: # curr is Null

            # get value from its parents right side
            temp= stack[-1].right

            # if parents right side is not null, assign curr to temp again
            if temp:
                curr=temp
            
            else: # no element to right, temp is also null

                # so stack top is going to be printed
                temp=stack.pop()
                res.append(temp.value)

                # if tree is right leaned pop out parent(root) elements and print
                while stack and temp==stack[-1].right:
                    temp=stack.pop()
                    res.append(temp.value)    
               
            

print("iterative postorder")
iterative_postorder(node)
print()