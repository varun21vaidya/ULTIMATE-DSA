# # Foundation Problems:

# # summation of first N numbers @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#  # parameterized way: TC:O(n) SC:O(n)
# def summation(n, summ):
#     if n < 1:
#         print("parameterized sum is ", summ)
#         return
#     summation(n-1, summ+n)

# summation(3, 0)


# # functinal way: TC:O(n) SC:O(n)
# def summation(n):
#     if n < 1:
#         return 0
#     return n+summation(n-1)

# print("functional sum is ", summation(3))


# # factorial of N: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # TC:O(n) SC:O(n)

# def facto(n):
#     if n<2:
#         return 1
#     return n*facto(n-1)

# n=5
# print("factorial of",n,"is equal to" ,facto(n))


# # reverse an Array: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # USING LOOPS

# arr=[2, 5, 8, 12, 23]
# for i in range(len(arr)//2):
#     arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
# print("using for loop", arr)


# arr=[2, 5, 8, 12, 23,45]
# i,j=0,len(arr)-1
# while i<j:
#     arr[i],arr[j]=arr[j],arr[i]
#     i+=1
#     j-=1
# print("using while",arr)


# # USING RECURSION /////////////////////////////////


# # WITH NEW ARRAY
# def reverser(arr,newarr):
#     if len(arr)==0: return
#     newarr.append(arr[len(arr)-1])
#     reverser(arr[:len(arr)-1],newarr)
#     return newarr
# arr=[2, 5, 8, 12, 23]
# newArr=[]
# print("using recursion with new arr",reverser(arr,newArr))


# # WITHOUT NEW ARRAY (Standard Approach) /////////////////////////////////
# def reverse_recursion(arr,i=0):
#     if i>=len(arr)//2: return
#     arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
#     # print("iteration",i,arr)
#     reverse_recursion(arr,i+1)
#     return arr
# arr=[1,2,3,4,5,6]
# print("using recursion",reverse_recursion(arr))


# # String Palindrome @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def pali_check(st,i=0):
#     # if index goes beyond half that means its palindrome
#     if i>=len(st)//2: return True
#     if st[i]==st[len(st)-1-i]:
#         return pali_check(st,i+1)
#     else:
#         return False
# st= "NAYAN"
# st2="1251"
# print(st,pali_check(st))
# print(st2,pali_check(st2))


# Fibonacci Number @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def fibo(n):
#     if n<2:
#         return n
#     return fibo(n-1)+fibo(n-2)

# n=6
# print(n,"th fibonacci number is",fibo(n))

# now when there was single recursion call,
# Complexity was TC:O(n) SC:O(n)
# but as there are two recursion calls,
# these two will call two more recursion calls
# So complexity will be Exponential ie, TC:O(2^n) (well not exact but general)
# And as maximum height of recursive tree is n, SC:O(n)


# Print All Subsequences @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# subsequence: a contigeous | non-contigeous sequence which follows the order

# arr=[3,1,2]
# contigeous = [3,1,2,(3,1),(1,2),(3,1,2)] # these are also subarrays
# non-contigeous= [(3,2)]
# but all in all order has to be maintianed

# USING POWER SET ALGORITHM (ie. BIT MANIPULATION)  (IMP**) ////////////////////////

# eg S='abc' --> "",a,b,c,ab,ac,bc,abc
# So if length of string is n, number of substrings generated are 2^n ***

# fundametal to check if bit is set or not
# suppose for number 4 --> 1 0 0 --> 0th bit=0, 1st bit =0, 2nd bit=1
# so to check if 2nd bit is set or not
# n & (1<<i), n=4 and i=2 for 2nd bit
# so if this gives non-zero number its set else its not set
# so if n & (i<<1)!=0  op=> set

# now for string of length n
# now for each number from 0 to 2^n -1 we will loop (2^n => (1<<n))
# and for each of that number we check if any of its bit is set or not
# if yes then add the value of that bit from original string

# eg for length of 3 ie abc where a=>0th bit, b=> 1st bit, c=>2nd bit
# 0 000 --> ""
# 1 001 --> a
# 2 010 --> b
# 3 011 --> ab
# 4 100 --> c
# 5 101 --> ac
# 6 110 --> bc
# 7 111 --> abc


# TC: O(2^n * n) SC: O(1)
# S="abc"
# n=len(S)
# for num in range((1<<n)):
#     sub=""
#     for i in range(n):
#         if num & (1<<i):
#             sub+=S[i]
#     print(sub)


# # ///////////////////////////////////////////////////////
# PROBLEM LINK: https://practice.geeksforgeeks.org/problems/power-set4302/1

# TC: O(2^n * n) SC: O(n)
# def AllPossibleStrings(self, s):
#     # Code here
#     n=len(s)
#     res=[]
#     for num in range(1<<n): # (2^n => (1<<n)) TC:O(2^n)
#         sub=""
#         for i in range(n):                    TC: O(n)
#             if num & (1<<i):
#                 sub+=s[i]
#         res.append(sub)
#     return sorted(res)[1:]


# USING RECURSION***** ////////////////////////////

# arr=[3,1,2] give all its subsequences

# for recursion we will use 2 parameters
# index to iterate, result for each subsequence
# For recursion the main condition we will first check
# if index we are increasing with each recursion tree
# is equal or greater than length of arr then print the resultant arr
# then take next value and append in result and use recursion
# now we also need to take conditions without that Value
# so remove that value from result and again use recursion
# this will use recursion until reaches end of index and check all conditions
# ad print all the subsequences

# TC: O(2^n) the recursion tree will need 2^n outputs
# SC: O(n) due to recursion stack
# as height of recursion tree will be same as lenght of input arr

# def printSubsequence(ind, arr,res):

#     if ind>=len(arr):
#         print(res)
#         return

#     # take value and use recursion
#     res.append(arr[ind])
#     printSubsequence(ind+1,arr, res)

#     # remove value and use recursion
#     res.remove(arr[ind])
#     printSubsequence(ind+1,arr, res)

# # Function call
# arr=[3,1,2]
# printSubsequence(0,arr,[])


# # Printing Subsequences whose sum is K @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# def printKSubsequence(ind, arr,res,k):

#     if ind>=len(arr):
#         if sum(res)==k:
#             print(res)
#         return

#     # take value and use recursion
#     res.append(arr[ind])
#     printKSubsequence(ind+1,arr, res,k)

#     # remove value and use recursion
#     res.remove(arr[ind])
#     printKSubsequence(ind+1,arr, res,k)

# # Function call
# arr=[1,2,1]
# printKSubsequence(0,arr,[],2)


# # Printing Subsequences whose sum is K but Only 1 value @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# # so when we get a value we return true
# # and when we get that value from a recursion == true
# # we will return true else false

# # in this sum => (s) is calculated along the way, either method is ok

# def printKSubsequence(ind, arr, res, k, s):

#     if ind >= len(arr):
#         if s == k:
#             print(res)
#             return True
#         else:
#             return False

#     # take value and use recursion
#     res.append(arr[ind])
#     s += arr[ind]
#     if (printKSubsequence(ind+1, arr, res, k, s) == True):
#         return True

#     # remove value and use recursion
#     res.remove(arr[ind])
#     s -= arr[ind]
#     if (printKSubsequence(ind+1, arr, res, k, s) == True):
#         return True

#     return False


# # Function call
# arr = [1, 2, 1]
# printKSubsequence(0, arr, [], 2, 0)


# # Count number of Subsequences whose sum is K @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # in this sum => (s) is calculated along the way

# # so for such problem where just count is enough
# # there is basic pattern

# # fn(){

# #     base case:
# #     true return 1
# #     false return 0

# #     call the left function
# #     l= f()

# #     call the right function
# #     r= f()

# #     return l+r
# # }

# # *******************************
# # (for multiple recursion calls, loop from 1 to n and before that s=0
# # and add the return values s+=f() and return s) USED FOR DP like N queens


# def printKSubsequence(ind, arr, k, s):

#     # s is sum variable like temp which we use to compare with
#     # k ie target sum

#     # if index reaches last element of array and if sum is equal to k
#     # return 1 which will increase the count cz we have found one subsequence
#     # if not return 0


#     # append one Element in sum and use recursion with increased index
#     # after adding this number if there is matched subsequence
#     # increase the count of left variable ie l

#     # after that remove that Element, and again use recursion to
#     # find another subsequence without that number
#     # if found it will increase count of right variable

#     # add both counts and return result


#     if ind >= len(arr):
#         if s == k:
#             return 1
#         else:
#             return 0

#     s += arr[ind]
#     l= printKSubsequence(ind+1, arr, k, s)

#     s -= arr[ind]
#     r= printKSubsequence(ind+1, arr, k, s)

#     return l+r


# # Function call
# arr = [1, 2, 1]
# print(printKSubsequence(0, arr, 2, 0))


# Combination Sum @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# PROBLEM LINK: https://leetcode.com/problems/combination-sum/


# so as this problem contains the structure of array of digits leading to target sum
# so similar to subsequnce problems we can use recursion by increasing index
# and adding a number calculating with recursion if its included in any subsequence
# then removing the same number and calculating recursion for matching subsequences
# without that number both conditions with increasing index untill lenght of original array

# now for this problem we are allowed to use same number unlimited times
# so we have to remember that we have to include same number in recursion
# by keeping the same index
# but to avoid the infinite loop, we have to reduce the target with that number
# and also check if that number is still less than target
# cz if target become less than current number, it will become negative

# now we have tried adding the same number few times now
# if the target value is equal to zero, we will add the temp arr ie subsequence
# to the resultant array which will give output

# but if the target becomes less than current value,
# we will avoid further recursion with that number and increase index
# but before that remember to remove the element after previous recursion ended

# so recursion will flow like this
# first declare global result array
# call the function with temp= empty array and ind=0 along with arr and target

# if the base condition ie ind is equal to len(arr)
# and target becomes zero (as we are reducing target in recursion)
# copy of temp will be stored in result array

# the value at index if less than target will be added to temp
# and use recursion with target - that value and keep index same
# now after all those inside recursions when the recursion ends
# remove the last added value
# and use recursion for next index

# at the end we will get result array


# def Combination_sum(ind, arr, target, temp):

#     # base condition
#     if ind == len(arr):
#         if target == 0:
#             # print("inserted",temp)
#             final.append(temp[:])
#         return

#     if arr[ind] <= target:
#         temp.append(arr[ind])
#         # print(temp)
#         Combination_sum(ind, arr, target-arr[ind], temp)
#         temp.pop()
#         # print("popped",temp)
#     Combination_sum(ind+1, arr, target, temp)


# candidates = [2, 3, 6, 7]
# target = 7
# final = []
# Combination_sum(0, candidates, target, [])
# print(final)


# # Combination Sum 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # problem link: https://leetcode.com/problems/combination-sum-ii/

# def combinationSum2(candidates, target):
#     def helper(ind, tempArr, target, res):

#         if target == 0:
#             res.append(list(tempArr))
#             return

#         for i in range(ind, len(candidates)):

#             # imp condition to avoid duplicates as for same numbers
#             # like 1 1 1 2 2, for recursion tree first 1 will start
#             # when it moves it doesnot matter if its first one or second one
#             # so only initial one is enough so it checks
#             # if i>ind ie its not first one and is same as previous one then skip it
#             if (i > ind and candidates[i] == candidates[i-1]):
#                 continue

#             if candidates[i] > target:
#                 break

#             tempArr.append(candidates[i])
#             helper(i+1, tempArr, target-candidates[i], res)
#             tempArr.pop()

#     candidates.sort()
#     res = []
#     helper(0, [], target, res)
#     return res


# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8
# print(combinationSum2(candidates, target))


# # Subset Sum 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # problem link: https://practice.geeksforgeeks.org/problems/subset-sums2234/1

# # a subset is subsequnce plus empty set


# # TC: O(2^n*n) SC: O(n) extra n in tc due to 'sum'
# def helper(ind, arr, res, temp):

#     if ind >= len(arr):
#         res.append(sum(temp))
#         return

#     temp.append(arr[ind])
#     helper(ind+1, arr, res, temp)

#     temp.pop()
#     helper(ind+1, arr, res, temp)


# arr = [3, 2, 1]
# ind, temp, res = 0, [], []
# helper(ind, arr, res, temp)
# print(sorted(res))


# # TC: O(2^n) SC: O(n) #instead of keeping array we just need sum value
# def helper(ind, arr, res, temp):

#     if ind >= len(arr):
#         res.append(temp)
#         return

#     # pick the element
#     # temp += arr[ind]
#     # helper(ind+1, arr, res, temp)

#     # not pick the element
#     # temp -= arr[ind]
#     # helper(ind+1, arr, res, temp)

#     # or this can be shortened by directly adding for that specific recursive call
#     # for next call, not add it ie not pick it

#     helper(ind+1, arr, res, temp+arr[ind])

#     helper(ind+1, arr, res, temp)


# arr = [3, 2, 1]
# ind, temp, res = 0, 0, []
# helper(ind, arr, res, temp)
# print(sorted(res))


# # Sub Sets 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # problem link:https://leetcode.com/problems/subsets-ii/

# # # TC: O(n*2^n) SC: O(n) #extra time for conversion to tuple
# def helper(ind, arr, res, temp):
#     if ind >= len(arr):
#         res.add(tuple(temp[:]))
#         return
#     temp.append(arr[ind])
#     helper(ind+1, arr, res, temp)
#     temp.pop()
#     helper(ind+1, arr, res, temp)

# ind, res, temp = 0, set(), []
# nums.sort()
# helper(ind, nums, res, temp)
# return res


# # Without Using set ie without extra N

# def helper(ind, temp):
#     # when recursion is called temp is added to resultant array
#     res.append(temp.copy())

#     for i in range(ind, len(nums)):
#         if i != ind and nums[i] == nums[i-1]:
#             continue

#         temp.append(nums[i])
#         helper(i+1, temp)
#         temp.pop()


# nums = [1, 2, 2]
# nums.sort()
# ind, res, temp = 0, [], []
# helper(ind, temp)
# print(res)


# # Permutations @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # Problem link: https://leetcode.com/problems/permutations/


# #         first of all we need a temp arr to store each permutation
# #         and we will also need a way to keep track of which number is already in temp
# #         so we will use map to check if its in temp arr or not

# #         so when we add a number in temp we will set its map value to 1
# #         and after recursions we will reduce it to 0 when we pop from temp

# #         so flow will be as follows
# #         before that define base case which will be
# #         if the len of temp is equal to input arr, its a permutation
# #         now we will loop through each number to check if its in temp arr using mapp
# #         if its not there append it to temp, and set its value in map as 1
# #         then to append the next set of digits call recursion with updated temp and mapp
# #         when all numbers are added base condition will be satisfied
# #         store that permutation and return to exit that recursion call
# #         for next permutation we will need to rearrange the digits
# #         so pop the recent digit and set its value as 0 in mapp

# #         now this loop will continue and recursion will move
# #         and we will get all permutations

# # TC: O(n!*n) permutations and loop
# # SC: O(n) to store the temp arr + depth of recursion tree

# def permute(nums):

#         def helper(temp,mapp):
#             if len(temp)==len(nums):
#                 return res.append(temp[:])

#             for i in nums:
#                 if not mapp[i]:
#                     temp.append(i)
#                     mapp[i]=1
#                     helper(temp,mapp)
#                     x=temp.pop()
#                     mapp[x]-=1


#         temp,mapp=[],{i:0 for i in nums}
#         res=[]
#         helper(temp,mapp)
#         return res

# nums=[1,2,3]
# print(permute(nums))
# # OP: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


#         now we can also solve this question without using extra map
#         instead we can just swap the digits in nums arr
#         for each level we will asign an index with which other digits will be swapped
#         and to swap all these index with specified index
#         we will loop from that index to len of nums
#         and after each swap call recursively for next level of index

#         now when these index will cross the len of nums we will store that permutation

#         and imp that we also have to reswap after each recursion
#         like we used to do pop from the temp arr after recursion

# TC: O(n!*n) permutations and loop
# SC: O(n)+O(n) addition to res arr + recursion tree

# def permute(nums):
#     def helper(ind,nums):
#         if ind>=len(nums):
#             # print(nums)
#             res.append(nums.copy())
#             return
#         for i in range(ind,len(nums)):
#             nums[ind],nums[i]=nums[i],nums[ind]
#             helper(ind+1,nums)
#             nums[ind],nums[i]=nums[i],nums[ind]

#     res=[]
#     helper(0,nums)
#     return res


# nums=[1,2,3]
# print(permute(nums))
# # OP: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# N - QUEENS @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # Problem-link
# # ans link by striver: https://takeuforward.org/data-structure/n-queen-problem-return-all-distinct-solutions-to-the-n-queens-puzzle/


# def solveNQueens(n):

#     def checker(row, col, board, n):

#         r,c=row,col

#         # check left side
#         while (c>=0):
#             if board[r][c]=="Q":
#                 return False
#             c-=1

#         # check left upward side
#         r,c=row,col

#         while (r>=0 and c>=0):
#             if board[r][c]=="Q":
#                 return False
#             c-=1
#             r-=1

#         # check left downward side
#         r,c=row,col
#         while (r<n and c>=0):
#             if board[r][c]=="Q":
#                 return False
#             c-=1
#             r+=1
#         return True

#     def queens(col,board,n):

#         if col==n:
#             # print(board)
#             ans.append(["".join(i) for i in board])
#             return

#         for row in range(n):
#             if checker(row,col,board,n):
#                 board[row][col]="Q"
#                 queens(col+1,board,n)
#                 board[row][col]="."

#     board=[["." for i in range(n)] for j in range(n)]
#     # print(board)
#     ans=[]
#     queens(0,board,n)
#     return ans

# n=4
# print(solveNQueens(n))


# # Optimized version where we can store the left_side, left_downwards, and left_upwards in array

# def solveNQueens(n):

#     def queens(col,board,n):

#         if col==n:
#             # print(board)
#             ans.append(["".join(i) for i in board])
#             return

#         for row in range(n):
#             if not left_side[row] and\
#             not left_downwards[row+col] and\
#             not left_upwards[(col-row)]:

#                 board[row][col]="Q"

#                 left_side[row]=1
#                 left_downwards[row+col]=1
#                 left_upwards[(col-row)]=1

#                 queens(col+1,board,n)
#                 board[row][col]="."

#                 left_side[row]=0
#                 left_downwards[row+col]=0
#                 left_upwards[(col-row)]=0

#     board=[["." for i in range(n)] for j in range(n)]
#     left_side=[0 for i in range(n)]
#     left_downwards=[0 for i in range(2*n-1)]
#     left_upwards=[0 for i in range(2*n-1)]
#     # print(board)
#     ans=[]
#     queens(0,board,n)
#     return ans

# n=4
# print(solveNQueens(n))


# # SUDOKU SOLVER @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # problem link: https://leetcode.com/problems/sudoku-solver/

# def solveSudoku(board):
#     """
#     Do not return anything, modify board in-place instead.
#     """

#     def isvalid(row, col, board, c):
#         # c is the number we want to check for this sudodku for that row,col position
#         c=str(c)
#         for i in range(9):

#             # check if c already is in same row
#             if board[row][i] == c:
#                 return False

#             # check if c already is in same col
#             if board[i][col] == c:
#                 return False

#             # check if c already is in same 3*3 box
#             # checks for every row and col from this box
#             if board[3 * (row // 3) + i//3][3 * (col//3) + i % 3] == c:
#                 return False

#         # if code comes to this level it means there has not been False
#         # ie c can be filled in board[row][col]
#         return True

#     # main function to solve sudoku
#     # traverse through matrix
#     for i in range(9):
#         for j in range(9):

#             # check if there is any empty cell
#             if board[i][j] == ".":

#                 # if there is any empty cell we will check for all values from 1 to 9
#                 for c in range(1, 10):

#                     # now call isvalid to check if c can be filled in board at i,j position
#                     if isvalid(i, j, board, c):

#                         # if isvalid is true then fill the c in the position
#                         # then we can use recursion to check if it can fulfill
#                         # for other empty cells or not if it fulfill we will not remove its value
#                         # and will return true
#                         # but if sudoku at any point in future for a certain position could not match
#                         # any value for that empty position then that will return False
#                         # and through backtracking we will come to this point which was wrong fill for this sudoku
#                         # so as it was wrong fill for this position then we will remove c from the board

#                         board[i][j] = str(c)

#                         if solveSudoku(board):
#                             return True
#                         else:
#                             board[i][j] = "."

#                 # even after checking for loop with isvalid from 1->9 for this position
#                 # if none of the value gets filled that means at some previous point it was wrong fill
#                 # so backtracking to that previous wrong fill point
#                 # it will return false which will return sodoku(board) to false and will empty that cell again
#                 # and check for next valid value for that position
#                 return False

#     # if it comes here, it means there is no empty cell remaining
#     return True

# Time complexity: for every cell ie n*n of matrix, we try to put number from 1->9
#                  ie 9 numbers tried for n*n matrix ie 9^(n*n) here n=3 ie 9^(3*3)
# Space complexity: n*n as that much stack space would be used


# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#          [".", "9", "8", ".", ".", ".", ".", "6", "."], [
#              "8", ".", ".", ".", "6", ".", ".", ".", "3"],
#          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], [
#              "7", ".", ".", ".", "2", ".", ".", ".", "6"],
#          [".", "6", ".", ".", ".", ".", "2", "8", "."], [
#              ".", ".", ".", "4", "1", "9", ".", ".", "5"],
#          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# # run the main sudoku function
# solveSudoku(board)
# print(board)


# # M-coloring Problem of Graph @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # Problem link: https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1


# #Function to determine if graph can be coloured with at most M colours such
# #that no two adjacent vertices of graph are coloured with same colour.
# def graphColoring(graph, M, N):

#     # we will check if a certain color can be applied to specific node
#     # such that it is not applied to adjecent nodes
#     # graph[node][i]==1 gives its adjecent node
#     # and if that color is applied to adjecent node return false
#     # else return True
#     def valid(col,node):
#         for i in range(N):
#             if graph[node][i]==1 and color[i]==col:
#                 return False
#         return True

#     def solve(node):
#         # if node is out of actual graph values,
#         # it means every function was True, ie we got solution
#         if node==N:
#             return True

#         # if there are M colors each color will be tried to apply to node
#         # if any of it is valid we check if can other colors be fitted to
#         # solution with this color, by recursing with next node
#         # if yes then return True
#         # if not then redefine that color to 0
#         for i in range(1, M+1):
#             if valid(i, node):
#                 color[node]=i
#                 if solve(node+1):
#                     return True
#                 else:
#                     color[node]=0

#         # if a certain node cannot be applied by any color
#         # then solution is wrong at some point in previous steps
#         # hence return true which will give false to solve(node+1)
#         # at that point and redifine the color to 0
#         return False

#     color=[0]*N
#     return solve(0)


# # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# # ADITYA VERMA PLAYLIST

# # ????????????????????????????????????????????????????????????????????????

# print numbers from 1 to N

# def printer(n):

#     if n==0:
#         return

#     # print (n)  # to print N to 1, print before recursive funciton to get max input then reach smallest recursively.
#     printer(n-1)
#     print(n) # to print 1 to N, print after recursive function to reach smallest input first
# n=5
# printer(n)


# # ????????????????????????????????????????????????????????????????????????

# def facto(n):
#     # base condition
#     if n == 0 or n == 1:
#         return n

#     # logic
#     return n*facto(n-1)


# print(facto(5))  # op: 120


# # ?????????????????????????????????????????????????????????????

# sort an array using recursion


# def sort(arr, n):

#   # Bubble Sort
#   # ITERATIVE SOLUTION
# for i in range(n):
#     for j in range(n-1-i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# return arr

# RECURSIVE SOLUTION
# if n==1:
#     return arr
# for j in range(n-1):
#     if arr[j] > arr[j+1]:
#         arr[j], arr[j+1] = arr[j+1], arr[j]

# return sort(arr, n-1)

#   # Insertion Sort
#   # Iterative Solution
# for i in range(1, n):
#     j=i-1
#     while j>=0 and arr[j]>arr[j+1]:
#         arr[j], arr[j+1] = arr[j+1], arr[j]
#         j=j-1

# return arr

# #   # Recursive Solution
# def insertion_sort(arr, i):

#     def insert(arr, j):
#         if j < 0 or arr[j] < arr[j+1]:
#             return arr
#         arr[j], arr[j+1] = arr[j+1], arr[j]
#         insert(arr, j-1)

#     if i == len(arr):
#         return arr

#     insert(arr, i-1)

#     insertion_sort(arr, i+1)

#     return arr

# # /////////////////////////////////////////////////

# # Alternate Method for Insertion Sort

# # can also be used to sort the stack recursively


# # to sort a stack we cant use traversal or swap
# # so all we have methods are pop or append on last index
# # so we will first remove last element from the stack
# # until there is only 1 element remaining, if it is return
# # then we will just have to check in next element and current element
# # so we just have to insert current element at correct position
# # so we will use another function just to insert the element at correct position
# # now if last element is less than current element just append current element on last position
# # or if there is no element in list then also append that element on last position
# # now if both are false, then we recursively put the current element at right position by
# # popping the last element of this list and then call insert funcition, and put that element
# # then finally append original,  last element at end which will sort the list


# def insert(arr, temp):

#     # to change the order ie decreasing just change the arrow dirction to >=
#     if len(arr) == 0 or arr[- 1] <= temp:
#         arr.append(temp)
#         return

#     val = arr.pop()
#     insert(arr, temp)
#     arr.append(val)


# def sortstack(arr):
#     if len(arr) == 1:
#         return
#     temp = arr.pop()
#     sortstack(arr)
#     insert(arr, temp)
#     return arr


# arr = [16, 6, 3, 8, 9, 4]
# # print(sort(arr, len(arr)))
# # print(insertion_sort(arr, 1))
# print(sortstack(arr))

# # OP: [3, 4, 6, 8, 9, 16]


# # ??????????????????????????????????????????????????????????????

# # Delete Middle Element of Stack

# from collections import deque
# import math


# def remove(dq):

#     def dele(dq, count):
#         if count == middle:
#             dq.pop()
#             # return midddle ele del stack
#             return dq

#         # untill then pop the elements recursively and
#         # after removing middle elements add them again
#         val = dq.pop()
#         dele(dq, count+1)
#         dq.append(val)
#         return dq

#     middle = math.ceil(len(dq)//2)
#     return dele(dq, 0)


# dq = deque([16, 6, 3, 8, 9, 4])
# print(remove(dq))
# dq = deque([16, 6, 3, 7, 8, 9, 4])
# print(remove(dq))

# # op:
# # deque([16, 6, 8, 9, 4])
# # deque([16, 6, 3, 8, 9, 4])


# # ????????????????????????????????????????????????????????????????????????

# # # Reverse a stack


# # To reverse a stack we will use two functions
# # first to pop each elemenet and second to place that element at initial position
# # ie first fn rev will pop each top element of stack until stack gets empty,
# # BASE COND: if stack gets empty return stack
# # now check insert function
# # now suppose eg is 3,2,1,7,6 this will pop 6 from stack and place it at start
# # ie  6 3 2 1 7, but how?  by poping len(st) numbers and
# # place 6 then again append all those numbers onntop of 6
# # now for next iteration we should pop top element 7 and insert it on 6
# # ie pop len(st)-1 numbers, add 7 to stack ie making it [6,7]
# # then again append all popped elements ie  6 7 3 2 1
# # now for next iteration get top element 1, pop len(st)-2 elements
# # and get stack as 6 7 1 3 2
# # now to do this kind of operation we need to reduce the count of numbers we need to pop
# # and that will be based on len(st), so here we use maxx as that variable
# # now during insertion we need to reach that maxx value and pop all those elements
# # so to track maxx we use count variable, and increase it for each pop operation
# # at the end when it reaches desired maxx value we append all those numbers

# def reverse(st):

#     def insert(st,temp,maxx,count):
#         if count==maxx:
#             st.append(temp)
#             return st
#         val=st.pop()
#         insert(st,temp,maxx,count+1)
#         st.append(val)

#     def rev(st, maxx):
#         if maxx==0:
#             return st
#         top= st.pop()

#         insert(st, top, maxx,0 )
#         return  rev(st, maxx-1)

#     return rev(st, len(st)-1)


# # //////////////////////////////////////////////////////////////

# # More simple trick
# # just after popping again recursively pop elements until there is only one element left
# # and then use insert function with popping untill stack gets empty and inserting
# # then append the last element on top of that

# # so combining both methods will result in recursively get top elements and then
# # recursively pop elements under it and append it on original first element
# # resulting in reversal of elements and final element will be under all those elements
# # so we will get total reversal of stack.

# def reverse(st):
#     def insert(st,temp):
#         if len(st)==0:
#             st.append(temp)
#             return st
#         val=st.pop()
#         insert(st,temp)
#         st.append(val)

#     def rev(st):
#         if len(st)==1:
#             return st
#         top= st.pop()
#         rev(st)
#         insert(st, top)
#         return st


#     return rev(st)


# from collections import deque
# st= deque([3,2,1,7,6])
# print(reverse(st))

# # OP: deque([6, 7, 1, 2, 3])


# # ????????????????????????????????????????????????????

# # K-th Symbol in Grammar
# # https://leetcode.com/problems/k-th-symbol-in-grammar/description/

# class Solution:
#     def kthGrammar(self, n: int, k: int) -> int:

#         # TLE

#         # if observed carefully, the result number is combination of
#         # its previous number and its compliment
#         # for 3 its "01" + "10" and "01" was 2
#         # for 4 its "0110" + "1001" and "0110" was 3 like that
#         # so we can recursively call the previous number
#         # and create its compliment or inverse and return the combination

# #         def solved(n):
# #             if n==1: return "0"

# #             s=solved(n-1)
# #             new=""
# #             for i in s:
# #                 new+=mapp[i]
# #             return s+new


# #         mapp={'0':'1','1':'0'}
# #         return solved(n)[k-1]

#         # similar approach just changed inverse method
#         # memory exceeded
# #         def solved(n):
# #             if n==1: return "0"

# #             s=solved(n-1)
# #             new=bin(int(s,2)^(2**(len(s)+1)-1))[3:]
# #             return s+new

# #         return solved(n)[k-1]

# #   WORKING SOLUTION:
# #     As we have seen that the output of n is double of complement of n-1,
# #     so the half of output of n is equal to previous
# #     so if k is before mid, we dont event need to calculate output of n, cz we can find the ans in n-1
# #     and if k is in next half we can calculate the ans by taking complement of that index from first half.
# #     but how to calculate mid, as we can see output numbers are powers of 2. ie
# #     for length= 2 to power n-1 ie for n=2, len= 2, n=3, len=4, for n=4, len=8 so length is just  2 to power of n-1
# #     and from that calculate the mid and find the ans.
# #     mid=(2**(n-1))//2

#     if n==1:
#         return 0

#     mid=2**(n-1) // 2

#     if k<=mid:
#         return self.kthGrammar(n-1,k)
#     else:
#         if self.kthGrammar(n-1,k-mid)==1:
#             return 0
#         else:
#             return 1


# # ??????????????????????????????????????????????????????????????

# # Tower Of Hanoi

# # def toh(N, fromm, to, aux):
# #     def solver(N, source, dest, helper):

# #         if N > 0:
# #             solver(N-1, source, helper, dest)
# #             print("move disk", N, "from rod", source, 'to rod', dest)
# #             solver(N-1, helper, dest, source)

# #     solver(N, fromm, to, aux)
# #     return (2**N)-1


#     def solver(N,source, dest, helper):

#         if N==1:
#             print("move disk", N, "from rod", source, 'to rod', dest )
#             return 1
#         count=solver(N-1, source, helper, dest)
#         print("move disk", N, "from rod", source, 'to rod', dest )
#         count+=solver(N-1, helper, dest, source)

#         return count+1

#     return solver(N, fromm, to, aux)

# # print(toh(3, 1, 2, 3))


# # ????????????????????????????????????????????????????????????????????

# # # Permutation with spaces:
# # Problem Link: https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1


# def permutation(S):
#     # code here
#     def solver(S, ind, temp, N):
#         if ind >= N:
#             ans.append(temp)
#             return

#         res1 = temp+S[ind]
#         solver(S, ind+1, res1, N)

#         res2 = temp+" "+S[ind]
#         solver(S, ind+1, res2, N)

#     ans = []
#     N = len(S)
#     solver(S, 1, S[0], N)
#     ans.sort()
#     return ans


# s = "ABC"
# print(permutation(s))


# # ????????????????????????????????????????????????????????????


# # # Permutations with Case Change
# # # https://www.geeksforgeeks.org/permute-string-changing-case/

# def caseChange(s):
#     def solver(s, temp, ind):
#         if ind >= len(s):
#             ans.append(temp)
#             return

#         solver(s, temp+s[ind], ind+1)
#         solver(s, temp+(s[ind].swapcase()), ind+1)

#     ans = []
#     solver(s, "", 0)
#     return ans


# s = "ab"
# print(caseChange(s))


# # # ????????????????????????????????????????????????????????????????

# # # Letter Change Permutation:
# # # https://leetcode.com/problems/letter-case-permutation/


# def caseChangeWithNum(s):
#     def solver(s, temp, ind):

#         if ind >= len(s):
#             ans.append(temp)
#             return

#         if s[ind].isnumeric():
#             solver(s, temp+s[ind], ind+1)
#         else:
#             solver(s, temp+s[ind], ind+1)
#             solver(s, temp+(s[ind].swapcase()), ind+1)

#     ans = []
#     solver(s, "", 0)
#     return ans


# s = [
#     "a1b2",
#     "3z4",
#     "123456",
#     "1239vX"]
# for i in s:
#     print(i, "=>", caseChangeWithNum(i))


# # ??????????????????????????????????????????????????????????????

# # Generate Balanced Parenthesis

# # https://leetcode.com/problems/generate-parentheses/

#     # first condition: total length will be 2*n
#     # so '(' will have maximum count of n, so as ')'
#     # addition condition: for '(' :
#     # ( can be added untill its count is upto n,
#     # and ) can be added if count of ')' is less than '('

#     # temp: temp string to add to final result
#     # ind: to count total length of string
#     # count1: count of '('
#     # count2: count of ')'

#     # base examples:
#     # for A=1 op: ()
#     # for A=2 op: (()), ()()


# def paranthesis(A):

#     def solver(temp, ind, count1,count2):
#         if ind>=2*A:
#             ans.append(temp)
#             return

#         if count1<A:
#             solver(temp+"(", ind+1, count1+1, count2)

#         if count2<count1:
#             solver(temp+")", ind+1, count1,count2+1)

#     ans=[]
#     solver("", 0,0,0)
#     return ans

# A=3
# ans=[]
# print(paranthesis(A))


# # ??????????????????????????????????????????????????????????

# # N Bit Binary Numbers having more '1's than '0's:
# # https://practice.geeksforgeeks.org/problems/print-n-bit-binary-numbers-having-more-1s-than-0s0252/1


# # brute force idea is to generate all binary numbers of given bit and filter those matching condition

# # function to generate all N-bit binary numbers
# def bin(digit, n):
#     arr = []
#     for i in range(digit):
#         arr.append(n % 2)
#         n = n >> 1

#     temp = ""
#     for ele in reversed(arr):
#         temp += str(ele)
#     return temp

# # function to generate all binary numbers of N digit.


# def generateAllBin(n):
#     high = int(pow(2, n))
#     for i in range(high):
#         res = bin(n, i)
#         print(res)


# ans = []
# generateAllBin(4)
# print(ans)

# now after we get all n bit codes, we just need to manipulate
# output according to condition
# but the whole code very exprensive


# # ///////////////////////////////////////////////////////////////////

# # SO just create only those values which match the condition, which is most efficient solution

# def NBitBinary(N):

#     # find binary number of N bits
#     # filter those numbers whose 1s are more than or equal to 0s
#     def printer(num, extra, remain):
#         if remain == 0:
#             ans.append(num)
#             return

#         printer(num+"1", extra+1, remain-1)

#         if extra > 0:
#             printer(num+"0", extra-1, remain-1)

#     strr = ""
#     ans = []
#     printer(strr, 0, N)
#     return ans


# N = 3
# print(NBitBinary(N))



# # /////////////////////////////////////////////////////////////


        
# we can also apply generate balanced parenthesis logic
# where instead of "(" and ")", we use '1'and '0'


#     # first condition: total length will be n
#     # so '1' will have maximum count of n
#     # addition condition: for '1' :
#     # 1 can be added untill its count is upto n,
#     # and 0 can be added if count of '0' is less than '1'

#     # temp: temp string to add to final result
#     # ind: to count total length of string
#     # count1: count of '1'
#     # count2: count of '0'

# def NBitBinary(n):

#     def solver(n,temp, count1,count2, ind):
#         if ind>=n:
#             ans.append(temp)
#             return
        
#         if count1<n:
#             solver(n, temp+"1", count1+1,count2, ind+1)
            
#         if count2<count1:
#             solver(n, temp+"0",count1,count2+1,ind+1)
            
#     ans=[]
#     solver(n, "", 0,0,0)
#     return ans

# N = 3
# print(NBitBinary(N))



# # ????????????????????????????????????????????????????????????????????

# # Joseph Problem:
# # https://practice.geeksforgeeks.org/problems/josephus-problem/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


# def josephus(n, k):

#     def kill(lst, k):
#         n = len(lst)
#         if n == 1:
#             return lst[0]

#         if n <= k:
#             ind = (k-1) % n
#         else:
#             ind = k-1
#         relist = lst[ind+1:]+lst[:ind]
#         return kill(relist, k)

#     persons = [i for i in range(1, n+1)]
#     return kill(persons, k)


# print("josephus problem", josephus(5, 2))  # op: 3
# print("josephus problem", josephus(7, 3))  # op: 4
