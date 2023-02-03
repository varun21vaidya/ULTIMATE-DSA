# Tree Template for Python

# Tree Node
from collections import deque
from collections import defaultdict


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

# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # # Preorder Traversal: root left right

# def preorder(root):
#     if root:
#         print(root.value, end=" ")
#         preorder(root.left)
#         preorder(root.right)

# print("preorder")
# preorder(node)


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # # Post Order Traversal: left right root

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.value, end=" ")

# print("postorder")
# postorder(node)
# print()


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


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


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # # Iterative Preorder Traversal (root left right):

# # Explanation:
# # to move iteratively we need to store the root nodes somewhere
# # USE LIFO ds ie stack to store left right nodes
# # Now as in preorder root left right, so when getting elements from stack
# # we will need left first then right, so insert right first then left
# # now suppose main root is inserted in stack, pop it and
# # append right and then left nodes to stack, then pop next element ie left
# # and get its right and left nodes...
# # when popping store those elements in saperate list as preorder treaversal

# def iterative_preorder(root):
#     if not root:
#         return
#     stack = [root]
#     ans = []
#     while stack:
#         currnode = stack.pop()
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


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


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
#     stack = []
#     res = []
#     currnode = root
#     while True:
#         if currnode:
#             stack.append(currnode)
#             currnode = currnode.left
#         else:  # currnode is null
#             if not stack:  # stack is empty
#                 break
#             currnode = stack.pop()
#             res.append(currnode.value)
#             currnode = currnode.right

#     print(res)
#     return res


# print("iterative inorder")
# iterative_inorder(node)
# print()


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # # Iterative Post Order (left root right)

# # # Explanation: 2 Stacks
# # to get postorder iteratively use 2 stacks
# # one for taking the current node from tree
# # then pop that node and add it to stack2
# # and add left and right nodes to stack1
# # now again get top element popped ie loop
# # now when stack1 gets empty we have traversed all the tree nodes
# # and those nodes are in stack2 in reverse order
# # so pop out values from that stack2 and add to result array
# def iterative_postorder(root):
#     st1 = [root]
#     st2 = []
#     res = []
#     while st1:
#         curr = st1.pop()
#         st2.append(curr)
#         if curr.left:
#             st1.append(curr.left)
#         if curr.right:
#             st1.append(curr.right)

#     while st2:
#         res.append(st2.pop().value)

#     print(res)
#     return res


# print("iterative postorder with 2 stacks")
# iterative_postorder(node)
# print()

# # # # ///////////////////////////////////////////////////////////////////

# # # # Explanation: 1 Stacks
# # # now we have to solve this using only 1 stack
# # # to do this we need to traverse to extreme left,
# # # until its null, and post the curr value to stack
# # # now when we reach the null go to else condition
# # # use temp to asign value at right side of top of the stack
# # # ie its parent nodes right side,
# # # ie we have checked all left node now its time to move right side
# # # if right side has value, assign it to curr, so it can traverse to its left
# # # and add those values to stack, until it becomes null again
# # # but that temp ie parents right node has no value ie null
# # # then pop the last element of stack ie last node of tree we covered and not printed yet.
# # # and that is value we need to add to result
# # # ie we have checked left then right now pop elements and get parent nodes
# # # then if that temp is part of right leaning subtree ie it is right side of its parent
# # # and if there is more such elements we can directly take all of them with a while loop
# # # so just check if temp is equal to top of stacks right element if it is
# # # then pop that top values and add it to result
# # # thats it, this whole code can cover if tree is going to left go to extreme left
# # # if found dead end, check parent nodes right subtree and make it current, ie go to that subtrees left then right
# # # now found dead end again? to right also ? pop from the stack which will be the values to be resulted
# # # if there is right leaning tree contineously pop elements and give result which will also include its parent nodes


# def iterative_postorder(root):

#     curr = root
#     temp = None
#     stack = []
#     res = []
#     while True:

#         # final condition, loop is not at beginnning
#         # and still stack become empty
#         if curr != root and not stack:
#             print(res)
#             return res

#         # if curr has value, add it to stack, move to its left values
#         if curr:
#             stack.append(curr)
#             curr = curr.left

#         else:  # curr is Null

#             # get value from its parents right side
#             temp = stack[-1].right

#             # if parents right side is not null, assign curr to temp again
#             if temp:
#                 curr = temp

#             else:  # no element to right, temp is also null

#                 # so stack top is going to be printed
#                 temp = stack.pop()
#                 res.append(temp.value)

#                 # if tree is right leaned pop out parent(root) elements and print
#                 while stack and temp == stack[-1].right:
#                     temp = stack.pop()
#                     res.append(temp.value)


# print("iterative postorder")
# iterative_postorder(node)
# print()


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # PREORDER, INORDER, POSTORDER in One Traversal:

# # # Explanation:
# # to get all preorder, inorder and postorder in one traversal
# # we need to make 3 list to contain them and one stack to store the root values and order
# # order is the order in which root values will be printed
# # for preorder root left right, so root will be printed 1st
# # for inorder left root right, so root will be printed 2nd
# # for postorder left right root, so root will be printed 3rd
# # so we will make a stack ie LIFO ds which stores [root, ord]

# # now initially stack will have main root and default order as 1
# # ie whenever we insert a new root it will have order as 1
# # run a while loop until our stack is empty
# # pop the top of the stack and get root and order
# # if order is 1, append root value to preorder, and make order =2
# # and reinsert the root, ord to stack
# # now if root has left subtree, update stack with that root ie [root.left, 1]

# # similarly when order is 2, add root.value to inorder and reinsert new root as root and 2 to stack
# # and if there is right subtree, update stack with that root ie [root.right,1]

# # for order equals to 3, just add root.value to postorder

# # TC: O(3N)
# # TC: O(4N)

# def pre_in_post(root):
#     stack=[[root,1]]
#     preorder, inorder, postorder= [],[],[]

#     while stack:
#         root,order= stack.pop()

#         if order==1:
#             preorder.append(root.value)
#             stack.append([root,2])

#             if root.left:
#                 stack.append([root.left,1])

#         if order==2:
#             inorder.append(root.value)
#             stack.append([root,3])

#             if root.right:
#                 stack.append([root.right,1])

#         if order==3:
#             postorder.append(root.value)

#     print('preorder',preorder)
#     print('inorder',inorder)
#     print('postorder',postorder)
#     return

# print("PREORDER, INORDER, POSTORDER in One Traversal")
# pre_in_post(node)
# print()


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # # Height of Binary Tree:

# # Problem LINK: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# # BFS ie Iterative way
# # increase counter at each level

# from collections import deque

# def height(root):
#     q=deque([root])
#     ans=0
#     if not root:
#         return ans
#     while q:
#         ans+=1
#         for i in range(len(q)):
#             temp=q.popleft()
#             if temp.left:
#                 q.append(temp.left)
#             if temp.right:
#                 q.append(temp.right)

#     return ans

# print()
# print("Height of Binary Tree")
# print(height(node))
# print()


# # # /////////////////////////////////////////////////////////////////


# # # Recursive Mode:
# # # go to left recursively, then go to right recursively
# # # when reached end ie root is null return 0 ie base condition
# # # at each recursion ie get max of left and right and add another level ie +1
# # # as we need to get max from left and right and we have already calculated it

# def height(root):
#     if not root: return 0

#     left=height(root.left)
#     right=height(root.right)

#     return max(left,right)+1


# print()
# print("Height of Binary Tree")
# print(height(node))
# print()


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # # Maximum Width of Binary Tree

# # # Problem Link: https://leetcode.com/problems/maximum-width-of-binary-tree/

# # # Explanation:

# # we implement bfs as its level order traversal
# # now for each level we have to increament double of previous
# # so for left we keep track of expected nodes ie actual node + null nodes
# # we will call it num, so for each next level we increase num by
# # num*2 for left and num*2+1 for right.
# # we will also keep track of previous level num
# # and at the end of each level we will check maximum width
# # and we can get current width by subtracting current num and old num+1
# # so calculate max width at each level and return ans


# def width(root):
#     if not root:
#         return 0
#     q = deque([[root, 1]])
#     maxwidth, num = 0, 1

#     while q:
#         old = q[0][1]

#         for i in range(len(q)):
#             temp, num = q.popleft()

#             if temp.left:
#                 q.append([temp.left, num*2])

#             if temp.right:
#                 q.append([temp.right, num*2+1])

#         maxwidth = max(maxwidth, num-old+1)

#     return maxwidth


# print()
# print("Width of Binary Tree")
# print(width(node))
# print()


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # # BALANCED BINARY TREE (Height Balanced)

# # # Problem LINK: https://leetcode.com/problems/balanced-binary-tree/

# # # Explanation:

# # first of all a balanaced binary tree means the height of left and right subtree
# # should not have difference of more than 1, at any node
# # yes, it means we have to calculate height of binary tree and at each point check
# # if the difference is larger if it is return -1
# # the calculation of determination of height is same as problem: depth of binary tree
# # ie : https://leetcode.com/problems/maximum-depth-of-binary-tree/
# # to improve complexity, check for -1 immedietly after left, so we can save space and time on right side
# # TC: O(N)  # N for traversing
# def isBalanced(root):

#     def solver(root):

#         if not root:
#             return 0

#         left = solver(root.left)
#         if left == -1:
#             return -1

#         right = solver(root.right)

#         if right == -1 or abs(left-right) > 1:
#             return -1

#         return max(left, right)+1

#     if not root:
#         return True  # for input = []

#     return solver(root) != -1

# print(isBalanced(node))


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # Diameter of Binary Tree
# # _______________________


# # Diameter of binary means maximum distance betwween two nodes
# # IT doesnt need to be passed through root.
# # The length of a path between two nodes is represented by the number of edges between them.

# # problem LINK: https://leetcode.com/problems/diameter-of-binary-tree/

# # Explanation:

# # Diameter of binary means maximum distance betwween two nodes
# # IT doesnt need to be passed through root.
# # The length of a path between two nodes is represented by the number of edges between them.
# # so it indicates that our solution requires the combination of left and right lenghts to be maximum for any node
# # so we can traverse and find for each node the depth of left subarray and depth of right subarray
# # and calculate the maximum by comparing the result with left subarray and right subarray.

# # TC: O(N*N) # Two recursive Functions


# def maxheight(root):
#     if not root: return 0

#     left= maxheight(root.left)
#     right= maxheight(root.right)

#     return max(left,right)+1

# def diam(root):
#     if not root:
#         return 0

#     left= maxheight(root.left)
#     right= maxheight(root.right)

#     return max(left+right, diam(root.left), diam(root.right))


# print("diaemeter of binary tree is",diam(node))

# # //////////////////////////////////////////////////////////////////////

# Modification
# as we saw depth calculate function is similar to main funciton
# ie we are unnecessarily traversing the tree again in main function
# instead we can just store the depth while traversing first time with a variable
# and get maximum depth from each node, and
# return the maximum length ie addition of  left and right

# TC: O(N) just one recursive function

# def diam(root):
#     def helper(root,maxi):
#         if not root: return 0

#         left= helper(root.left,maxi)
#         right= helper(root.right,maxi)
#         maxi[0]=max(maxi[0],left+right)
#         return max(left,right)+1

#     maxi=[0]
#     helper(root,maxi)
#     return maxi[0]

# print("diaemeter of binary tree is",diam(node))


# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # # Binary Tree Maximum Path Sum

# # # Problem LINK: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# # Explanation:
# # as we can see, we have to traverse and check if node can be part of optimal path
# # to check that we need to check on its left and right side
# # SO this is similar to calculate depth problem in dfs way
# # so similar to that traverse on left and right subtrees and if we get null return 0
# # and at the end check if left subtree can be part of path or right subtree
# # so get maximum of left, right along with current node value
# # so return node.value + max(left,right)

# # but we need to have result of maximum (sum of values of path )
# # so we will use variable maxi to calculate if current path sum is maximum or not
# # ie sum of current node plus its left and right nodes ie check max(maxi, node.val+left,right)
# # but there can be negative values also, to handle them check if left is negative, make it zero
# # and similarly for right.
# # finally return maxi
# def path(root):

#     def solver(root, maxi):

#         if not root:
#             return 0

#         left = solver(root.left, maxi)
#         right = solver(root.right, maxi)

#         if left < 0:
#             left = 0
#         if right < 0:
#             right = 0

#         maxi[0] = max(maxi[0], root.value+left+right)

#         return root.value + max(left, right)

#     maxi = [float('-inf')]
#     solver(root, maxi)
#     return maxi[0]


# print("Maximum Path of Binary Tree is: ", path(node))  # op 36


# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # # EQUAL TREES OR NOT:

# # # Problem LINK:https://leetcode.com/problems/same-tree/

# def isSameTree(p, q):

#     # if eiher or both are null check if both are null
#     if p==None or q==None:
#         return p==q

#     return (p.val==q.val) and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)


# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # Vertical Traversal:
# # PROBLEM LINK: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# def verticalTraversal(root):

# from collections import defaultdict
# # METHOD 1: USING BRUTE FORCE AND DFS
# def solver(root, col,level):
#     if not root: return

#     # mapp[col].append((level,root.value))

#     if col in mapp:
#         if level in mapp[col]:
#             mapp[col][level].append(root.value)
#         else:
#             mapp[col][level]=[root.value]

#     else:
#         mapp[col]={level: [root.value]}

#     solver(root.left,col-1,level+1)
#     solver(root.right,col+1,level+1)

# mapp={}
# solver(root,0,0)

# # print(mapp)
# # {0: {0: [1], 4: [6], 2: [10, 9]}, -1: {1: [2], 3: [5]}, -2: {2: [4]},
# # 1: {1: [3]}, 2: {2: [10]}}

# # after creating the data structure we will append those values in sorted order
# ans=[]
# for col in sorted(mapp.keys()):
#     temp=[]
#     for level in sorted(mapp[col].keys()):
#         temp+=sorted(mapp[col][level])
#     ans.append(temp)

# return ans

# #---------------------------------------------------------------

#         # METHOD 2: IMPROVISE DFS

# but its not at all efficient cz two loops + sorted !!

# so put everything in a single list and we will sort it

# def solver(root,col,level):
#     if not root: return

#     temp.append([col,level,root.value])

#     solver(root.left, col-1,level+1)
#     solver(root.right, col+1,level+1)

# temp=[]

# solver(root,0,0)

# # as we have already arranged in first col, then level, then root.val
# # sorting will take place in same order
# temp.sort()
# # this is temp structure now: temp= [[col,level,val]]

# # print(temp)

# # Create ans format
# res=[[temp[0][2]]]
# for i in range(1,len(temp)):
#     # if its same col as before add value to last added col
#     if temp[i][0]==temp[i-1][0]:
#         res[-1].append(temp[i][2])

#     # else create new col list and add value
#     else:
#         res.append([temp[i][2]])

# return res

# # -------------------------------------------------------------------------

# # METHOD 3: USING BFS

# ans=[]
# col,lev=0,0
# q=deque([[col,lev,root]])
# # print(q)
# while q:
#     for i in range(len(q)):
#         col,lev,temp=q.popleft()

#         if temp.left:
#             q.append([col-1, lev+1,temp.left])
#         if temp.right:
#             q.append([col+1,lev+1,temp.right])

#         ans.append([col,lev,temp.value])

# ans.sort()
# # print(ans)
# # # [[-1, 0, 9], [0, 0, 3], [0, 0, 15], [1, 0, 20], [2, 0, 7]]

# # Create ans format
# res=[[ans[0][2]]]
# for i in range(1,len(ans)):
#     # if its same col as before add value to last added col
#     if ans[i][0]==ans[i-1][0]:
#         res[-1].append(ans[i][2])

#     # else create new col list and add value
#     else:
#         res.append([ans[i][2]])

# return res


# print("vertical Traversal")
# print(verticalTraversal(node))


# #  # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # # Boundry of Binary Tree:
# # # PROBLEM LINK:https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

# def boundry(root):

#     def goleft(root):
#         if not root.left and not root.right:
#             return lefts
#         lefts.append(root.value)
#         if not root.left:
#             goleft(root.right)
#         goleft(root.left)

#     def leafnodes(root):
#         # inorder traversal as it gets leaf nodes from left to right correctly
#         if not root:
#             return
#         if not root.left and not root.right:
#             leafs.append(root.value)
#             return

#         leafnodes(root.left)
#         leafnodes(root.right)

#     def goright(root):
#         if not root.left and not root.right:
#             return rights
#         rights.append(root.value)
#         if not root.right:
#             goright(root.left)
#         goright(root.right)

#     lefts, leafs, rights = [], [], []
#     goleft(root)
#     # print(lefts)
#     leafnodes(root)
#     # print(leafs)
#     goright(root)
#     # print(rights)
#     ans = lefts+leafs+rights[::-1]
#     ans.pop()  # remove last element which is root again from right
#     return ans


# print("print boundry nodes of tree")
# print(boundry(node))


# #  # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # # TOP VIEW OF BINARY TREE
# # # PROBLEM LINK: https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


# # # Recursive Approach:
# # use dfs traversal and use a col and level variables that we used in vertical traversal
# # but here we just need to print the outermost ie top level nodes from each col so store those col and level in mapp
# # now traverse and check if that col in mapp and if its present from its values ie [level, root] check
# # if level in mapp is greater than current level if its not then update col with current level and root

# # here as we move downwards in the tree we will reduce level so it becomes easier to compare to get top level
# # and at the end sort the mapp keys and return values


# def TopViewQ(root):
#     def topview(root,col,level):
#         if not root: return

#         if col in mapp:
#             if level>=mapp[col][0]:
#                 mapp[col]=[level,root.value]
#         else:
#             mapp[col]=[level,root.value]

#         topview(root.left,col-1,level-1)
#         topview(root.right,col+1,level-1)


#     from collections import defaultdict
#     mapp=defaultdict(list)
#     topview(root,0,0)
#     # print(mapp)

#     return [mapp[x][1] for x in sorted(mapp)]

# print("TOP VIEW OF BINARY TREE")
# print(TopViewQ(node))

# # # /////////////////////////////////////////////////////////////

# # Iterative Appraoch:
# # similar to dfs we just replace it with bfs


# def TopViewQ(root):

#     import collections
#     mapp=collections.defaultdict(list)
#     q=collections.deque([[root,0,0]])
#     while q:
#         for i in range(len(q)):
#             temp,col,level=q.popleft()

#             if temp.left:
#                 q.append([temp.left,col-1,level-1])
#             if temp.right:
#                 q.append([temp.right,col+1,level-1])

#             if col in mapp:
#                 if level>=mapp[col][0]:
#                     mapp[col]=[level,temp.value]
#             else:
#                 mapp[col]=[level,temp.value]

#     # print(mapp)

#     return [mapp[x][1] for x in sorted(mapp)]

# print("TOP VIEW OF BINARY TREE")
# print(TopViewQ(node))

# # # FOR BOTTOM JUST change level-1 to level+1
# # # so levels would be changed accordingly and highest level is bottom one is shown

#  # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # BINARY TREE RIGHT SIDE VIEW
# # PROBLEM LINK: https://leetcode.com/problems/binary-tree-right-side-view/

# def rightSideView(root):

# # Iterative ie BFS: Intuitive
# if not root: return
# q=deque([root])
# ans=[]
# while q:
#     for i in range(len(q)):
#         temp=q.popleft()
#         if temp.left:
#             q.append(temp.left)
#         if temp.right:
#             q.append(temp.right)

#     ans.append(temp.value)
# return ans

# # # ////////////////////////////////////////////////////////

# Recursive ie DFS
# take level variable and increase it with each subtree
# and as we move we will store the level: root.value in mapp
# now as we are moving first to left then to right
# the last updated value for that level would be from right only
# so just return the hashmap values in a list

# def dfs(root, level):
#     if not root:
#         return

#     mapp[level] = root.value

#     dfs(root.left, level+1)
#     dfs(root.right, level+1)

# mapp = defaultdict(int)
# dfs(root, 0)
# # print(mapp)

# return mapp.values()


# # for left subtree just take right side traversal
# # then left side traversal

#     def dfs(root, level):
#         if not root:
#             return

#         mapp[level] = root.value

#         dfs(root.right, level+1)
#         dfs(root.left, level+1)

#     mapp = {}
#     dfs(root, 0)
#     # print(mapp)

#     return mapp.values()


# print("Print Right side view of Tree")
# print(rightSideView(node))


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # # SYMMETRIC TREES
# # # Problem LINK : https://leetcode.com/problems/symmetric-tree/


# # Explantiion:
# # Mirrored tree means for the root node
# # the left side will traverse with suppose root left right
# # while right subtree will traverse with root right left
# # and we have to traverse them at the same time
# # if one of the nodes is null, other has to be, if its not return False
# # both the nodes from left subtree and right subtree should be of same value to be symmetric

# def isSymmetric(root):

#     def solver(left, right):

#         if not left or not right:
#             return left == right

#         if left.value != right.value:
#             return False

#         return solver(left.left, right.right) and solver(left.right, right.left)

#     if not root:
#         return
#     return solver(root.left, root.right)


# print("check if Trees are symmetric or not")
# print(isSymmetric(node))


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# # # Path to Given Node
# # # __________________

# # Problem LINK: https://www.interviewbit.com/problems/path-to-given-node/

# # Explanation:
# # so first we will create a recursive function, and use it to traverse from left and then right and
# # then check if it meets the goal or not and store those nodes in between
# # and if we observe that the further is deadend and we are returning without meeting goal
# # we remove such unnecessary nodes from our path

# # Now first take the base condition, if root is Null return False
# # and now append the node value to ans array
# # and check if the root value is goal or not if we met goal return True
# # then we will use boolean values for left and right traversal
# # if both of them are false both left and right traversals are useless
# # so popout the last appended node
# # but if any of them has met goal, that is correct path, so return True
# # finally return the ans array path.

# def path(A, B):

#     def solver(root, goal):
#         if not root: return False

#         ans.append(root.value)

#         if root.value==goal:
#             return True

#         a=solver(root.left,goal)
#         b=solver(root.right,goal)

#         if not (a or b):
#             ans.pop()
#             return False
#         else:
#             return True

#     ans=[]
#     solver(A, B)
#     return ans

# print("Path to given Node 8")
# print(path(node, 8))


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # Lowest Common Ancester:

# # problme LINK: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree


#     # we will go to the path from root to each p and q
#     # how will we do that, check this out
#     # # Problem LINK: https://www.interviewbit.com/problems/path-to-given-node/

#     # # Explanation:
#     # # so first we will create a recursive function, and use it to traverse from left and then right and
#     # # then check if it meets the goal or not and store those nodes in between
#     # # and if we observe that the further is deadend and we are returning without meeting goal
#     # # we remove such unnecessary nodes from our path

#     # # Now first take the base condition, if root is Null return False
#     # # and now append the node value to ans array
#     # # and check if the root value is goal or not if we met goal return True
#     # # then we will use boolean values for left and right traversal
#     # # if both of them are false both left and right traversals are useless
#     # # so popout the last appended node
#     # # but if any of them has met goal, that is correct path, so return True
#     # # finally return the ans array path.


#     # # now we got paths for q and q then from those paths we got that
#     # # from root to some node both the paths were identical and at some point both saperated
#     # # at this point is our common ancestor
#     # # so we will traverse through both paths and check when they saperates ie their values differs
#     # # so we will return node before that point

#     # # But there are conditions like  a node to be a descendant of itself, in this case
#     # # one of the paths itself will end first so just return last node of that path

# def LCA(root,p,q):

#     def path(root,goal,ans):

#         if not root: return False

#         if root==goal:return True

#         if path(root.left,goal,ans) or path(root.right,goal,ans)
#             return True
#         else:
#             ans.pop()
#             return False

#     pathp,pathq=[],[]
#     i,j=0,0
#     while i<len(pathp) and j<len(pathq):
#         if pathp[i]!=pathq[j]:
#             return pathp[i-1]
#         i+=1
#         j+=1

# #   # when one of i, or j reaches end it means its last element was common node

#     if i==len(pathp): return pathp[-1]
#     if j==len(pathq): return pathq[-1]


# # # ////////////////////////////////////////////////////////////////////////////

# # # # IMPROVED VERSION - WITHOUT USING EXTRA SPACE

# # like we traversed left and right nodes, we will traverse again
# # but whenever we reach one of p or q, we will return that p or q
# # else we will return a null if we reach null
# # and at each node we will check if the returned node is null or p or q
# # if any one of them is null return other ie if left is null return right
# # now even if right is also null, we anyway had to return null
# # but if right has value of p or q, it will return that
# # now if left has value and right is null, return left
# # but if both of them has value then we have got the solution node
# # so return that node

# # But there are conditions like a node to be a descendant of itself, in this case
# # suppose there is root node 3 on left there is 4 and right of it is 5-->6 and
# # we had to find for 5 , 6 only, then from left 4 is not one of them, returns null
# # on right we got 5 which is one of them, so returns 5, and 3 will return 5 only
# # so if you observe, the code returns first occured p or q , and it will be LCA only.


# def DCA(root, p, q):
#     def solver(root):
#         # if not root: return root # # ie return Null
#         # if root==p: return p
#         # if root==q: return q
#         # # instead we can just combine them

#         if not root or root==p or root==q:
#             return root

#         left=solver(root.left)
#         right=solver(root.right)

#         if not left: return right
#         elif not right: return left
#         else:
#             return root

#     return solver(root)


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # # All nodes distance from K:

# # # PROBLEM LINK: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# def distanceK(root, target, k):

#     def addmap(root,parent):
#             if not root: return

#             mapp[root]=parent
#             addmap(root.left,root)
#             addmap(root.right,root)
#     mapp=defaultdict(int)
#     addmap(root,None)


#     # # USING DFS:

#     def solver(root,dist):
#         if not root or root in visited :return

#         visited.add(root)
#         if dist==k:
#             res.append(root.value)
#             return

#         solver(root.left,dist+1)
#         solver(root.right,dist+1)
#         solver(mapp[root],dist+1)

#     res=[]
#     visited=set()
#     solver(target,0)
#     return res

# #     # # USING BFS:

# #     q=deque([[target,0]])
# #     visited=set()
# #     visited.add(target)
# #     while q:
# #         # print("tree",[(node.val,d) for node, d in q])
# #         if q[0][1]==k: return [node.value for node, d in q]

# #         temp,dist= q.popleft()
# #         for node in (temp.left,temp.right,mapp[temp]):
# #             if node and node not in visited:
# #                 visited.add(node)
# #                 q.append([node,dist+1])
# #         # print("visited",[x.val for x in visited])

# #     return []

# print("All nodes distance from K")
# k=2
# print(distanceK(node,node,2))


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # # Problem Link: https://practice.geeksforgeeks.org/problems/burning-tree/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


# def minTime(root, target):
#     # code here
#     def getparent(root, parent):
#         if not root:
#             return

#         parents[root] = parent

#         getparent(root.left, root)
#         getparent(root.right, root)

#     import collections
#     parents = collections.defaultdict(int)
#     getparent(root, None)

#     visited = {target}
#     res = 0
#     goal = root

#     def gettotarget(root):
#         if not root:
#             return
#         if root.value == target:
#             nonlocal goal
#             goal = root
#         gettotarget(root.left)
#         gettotarget(root.right)

#     gettotarget(root)

#     q = collections.deque([[goal, res]])
#     while q:
#         res = q[0][1]
#         node, dist = q.popleft()
#         for temp in (node.left, node.right, parents[node]):
#             if temp and temp.value not in visited:
#                 visited.add(temp.value)
#                 q.append([temp, dist+1])
#     return res


# print("Burning Tree")
# print(minTime(node, 8))


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # Construct a Binary Tree from Inorder and Preorder

# # Problem Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# def construct(preorder,inorder):

#     # # Explantion:
#     # # 1. inorder means left root right
#     # # 2. preorder means root left right
#     # # 3. so preorder will take the root but it cant get how many
#     # #     elements are in its left node or right node
#     # # 4. so thats where inorder comes, it gives elements to its left and
#     # #     right , so take the element from preorder, find its index in
#     # #     inorder
#     # # 5. and assign the left and right subtrees to with new preorder and
#     # #     inorder with size of index
#     # # 6. for left inorder would be elements on its left ie 0 to ind
#     # #     and for preorder add that index apart from currnt index 1:ind+1
#     # # 7. for right, inorder would be right side elements of that index
#     # #     ie ind+1 to end
#     # #     and for preorder again from index +1 to end
#     # # 8. finally return the newly created node with left and right
#     # #       subtrees

#     # def builder(preorder,inorder):
#     #     if not preorder or not inorder:
#     #         return
#     #     tr=Node(preorder[0])
#     #     ind= inorder.index(preorder[0])

#     #     tr.left= builder(preorder[1:ind+1],inorder[:ind])
#     #     tr.right= builder(preorder[ind+1:],inorder[ind+1:])

#     #     return tr
#     # return builder(preorder,inorder)


#     # # # /////////////////////////////////////////////////////////////////

#     # Improving the Solution:

#     # Now instead of using heavy operations by creating new list everytime
#     # we will just take indexes and arrange them to get the same effect of
#     # creating the new list, ie make prestart,preend,instart,inend variables

#     # Now to improve finding index each time just use hashmap to store all the
#     # index of inorder nodes, ie for creting node, take prestart
#     # ie starting index of prestart and get its index from map.

#     # now when we calculate index get, remaining numbers from starting of inorder to index
#     # ie that index - starting index of inorder naming it remain

#     # now for left and right nodes,
#     # left: for prestart+1 ie next of current node to prestart+remain, take that many elements from left
#     # and for inorder, take from starting of inorder upto index calculated ie instart to getind-1
#     # right: for starting of preorder + number of elements on left to end of preorder
#     # for inorder, from next of current index to end of inorder.

#     def build(preorder,prestart,preend,inorder,instart,inend):
#         if prestart>preend and instart>inend:
#             return
#         tr=Node(preorder[prestart])
#         getind= mapp[preorder[prestart]]
#         remain= getind-instart
#         tr.left= build(preorder,prestart+1,prestart+remain,inorder,instart,getind-1)
#         tr.right=build(preorder,prestart+remain+1, preend,inorder, getind+1, inend)

#         return tr

#     mapp=dict()
#     for i in range(len(inorder)):
#         mapp[inorder[i]]=i

#     return build(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)


# print("Construct a Binary Tree from Inorder and Preorder")
# preorder=[3,9,20,15,7]
# inorder=[9,3,15,20,7]
# x=construct(preorder,inorder)
# print2D(x)


# # # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# # Morris Traversal: Iterative INORDER in O(1) Space:

def Morris(root):

    curr = root
    while curr != None:
        if curr.left:

            new = curr.left

            # first go to next left
            # then go to its rightmost element and check
            # 1.if new.right is not pointing to current element
            # ie if it is then we have already traversed here
            # 2. if its first time in this node, run loop until
            # it reaches null, traverse to rightmost position
            # 3. after that check if there was link previously,
            # if there was, go to right subtree of current
            # ie covered left subtree
            # 4. else if its first time, go into left subtree and
            # also make that link from rightmost to current parent node

            while new.right != curr and new.right != None:
                new = new.right

            # we had already traversed here, print and go to right subtree
            if new.right == curr:
                new.right=None
                print(curr.value, end=" ")
                curr = curr.right

            else: # curr is null ie first time here
                new.right = curr
                curr = curr.left

        else:
            # if we reached left deadend, print current node and move right
            print(curr.value, end=" ")
            # res.append(curr.val)
            curr = curr.right


res = []
print("The morris Traversal is")
Morris(node)
