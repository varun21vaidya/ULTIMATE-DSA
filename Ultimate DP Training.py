# # DP: Enhansed Recursion

# # HOW TO IDENTIFY:
# # 1>>>> There will be choice - RECURSION IS USED
# #         --and if there is overlapping then DP IS USED
# #              -- but if recursion is calling only one function then DP is not used
# #              -- but if two functions are called there is chance that, for some function
# #              -- there is already calculated solution of this function from previous recursion


# # 2>>>> Optimal is asked ie min or max

# # steps:
# # 1. Write recursive function and use memoization
# # 2. TOP DOWN Approach -(BUT DONT WRITE TOP DOWN WITHOUT THINKING RECURSIVE SOLUTION)

# # Parent PROBLEMS TO SOLVE:
# # 1. 0-1 knapsack
# # 2. Unbounded Knapsack
# # 3. Fibonacci
# # 4. LCS
# # 5. LIS
# # 6. Kadane Algorithm
# # 7. Matrix Chain Multiplication
# # 8. DP on Trees
# # 9. DP on Grid
# # 10. Others


# # 1. 0-1 Knapsack Problem
# # SUBPROBLEMS:

# # 1. subset sum
# # 2. equal sum partition
# # 3. count of subset sum
# # 4. minimum subset sum difference
# # 5. target sum
# # 6. number of subset of given difference


#                             _____ fractional Knapsack (not DP but GREEDY)
#                             |
# # # 3 TYPES OF KNAPSACK ----|--- 0/1 Knapsack
#                             |____UnBounded Knapsack


# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # 0/1 Knapsack:
# # Problem LINK: https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
# # Function to return max value that can be put in knapsack of capacity W.
# def knapSack(self,W, wt, val, n):

# #   RECURSIVE APPROACH:
#     # def solver(W, wt, val, n):
#     #     if n==0 or W==0:
#     #         return 0

#     #     if wt[n-1]<=W:
#     #         return max(val[n-1]+ solver(W-wt[n-1], wt, val, n-1),
#     #         solver(W, wt, val, n-1))

#     #     else:
#     #         return solver(W, wt, val, n-1)

#     # return solver(W, wt, val, n)

# # DYNAMIC PROGRAMMING - MEMOIZATION
#     # def solver(W, n):
#     #     if n==0 or W==0:
#     #         return 0

#     #     if dp[n][W]!=-1:
#     #         return dp[n][W]

#     #     if wt[n-1]<=W:
#     #         dp[n][W]=max(val[n-1]+ solver(W-wt[n-1], n-1),
#     #         solver(W, n-1))

#     #     else:
#     #         dp[n][W]= solver(W, n-1)

#     #     return dp[n][W]

#     # dp=[[-1 for _ in range(W+1)] for _ in range(n+1)]
#     # # print(dp)
#     # return solver(W,n)

#     # DP - BOTTOM UP APPRAOCH
#     dp=[[0]*(W+1) for _ in range(n+1)]
#     for row in range(1,n+1):
#         for col in range(1,W+1):
#             # replace n,W with row and col
#             if wt[row-1]<=col:
#                 dp[row][col]= max(val[row-1]+ dp[row-1][col-wt[row-1]], dp[row-1][col])

#             else:
#                 dp[row][col]=dp[row-1][col]

#     return dp[-1][-1]


# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# # SUBSET SUM
# # PRBLEM LINK: https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# def isSubsetSum ( N, arr, sum):
#     # code here

#     # # Recursive:

#     # def solver(n,w):
#     #     if n==0: return False
#     #     if w==0: return True
#     #     if arr[n-1]<=w:
#     #         return solver(n-1, w-arr[n-1]) or solver(n-1,w)
#     #     else:
#     #         return solver(n-1, w)

#     # return solver(N,sum)


#     # # Memoization
#     # def solver(n,w,dp):
#     #     if n==0: return False
#     #     if w==0: return True

#     #     if dp[n][w]!=-1:
#     #         return dp[n][w]

#     #     if arr[n-1]<=w:
#     #         dp[n][w]= solver(n-1, w-arr[n-1],dp) or solver(n-1,w,dp)
#     #     else:
#     #         dp[n][w]= solver(n-1, w,dp)

#     #     return dp[n][w]

#     # dp=[[-1 for _ in range(sum+1)] for _ in range(N+1)]
#     # return solver(N,sum,dp)


#     # # Bottom Up Approach

#     dp=[[0 for _ in range(sum+1)] for _ in range(N+1)]
#     # for weight =0 there always be True
#     for firstcol in range(N+1):
#         dp[firstcol][0]=1

#     for row in range(1,N+1):
#         for col in range(1,sum+1):
#             if arr[row-1]<=col:
#                 dp[row][col]=dp[row-1][col-arr[row-1]] or dp[row-1][col]
#             else:
#                 dp[row][col]= dp[row-1][col]

#     return dp[N][sum]


# print("subset sum ans")
# N=6
# arr=[3, 34, 4, 12, 5, 2]
# sum=9
# print(isSubsetSum ( N, arr, sum))
# sum=30
# print(isSubsetSum ( N, arr, sum))


# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# # PARTITION EQUAL SUBSET SUM
# # PROBLEM LINK: https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1

# def equalPartition( N, arr):
#     # code here

#     # # Memoization

#     # def solver(n,w):
#     #     if n==0:
#     #         return 0
#     #     if w==0:
#     #         return 1

#     #     if dp[n][w]!=-1:
#     #         return dp[n][w]
#     #     if arr[n-1]<=w:
#     #         dp[n][w]= solver(n-1, w-arr[n-1]) or solver(n-1, w)
#     #     else:
#     #         dp[n][w]= solver(n-1, w)

#     #     return dp[n][w]

#     # w=sum(arr)
#     # if w%2==1:
#     #     return False
#     # else:
#     #     w=w//2
#     #     dp=[[-1 for _ in range(w+1)]for _ in range(N+1)]
#     #     return solver(N,w)


#     # # Bottom Up Apprach

#     w=sum(arr)
#     if w%2==1:
#         return 0
#     w=w//2
#     dp= [[0 for _ in range(w+1)] for _ in range(N+1)]
#     for firstcol in range(N+1):
#         dp[firstcol][0]=1

#     for row in range(1,N+1):
#         for col in range(1,w+1):
#             if arr[row-1]<=col:
#                 dp[row][col]=(dp[row-1][col- arr[row-1]]  or dp[row-1][col])
#             else:
#                 dp[row][col]=dp[row-1][col]
#     return dp[N][w]


# print("partition equal subset sum")
# N=4
# arr=[1, 5, 11, 5]
# print(equalPartition( N, arr))
# N=3
# arr=[1,3,5]
# print(equalPartition( N, arr))


# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # # COUNT OF SUBSET SUM

# def subsetSumCount(n, arr, w):

#     def solver(n,w,count):
#         if n==0:
#             if w==0:
#                 count+=1
#             return count

#         if arr[n-1]<=w:
#             count=solver(n-1,w-arr[n-1],count)+solver(n-1,w,count)

#         else:
#             count= solver(n-1,w,count)

#         return count
#     count=0
#     return solver(n, w,count)

#     dp = [[0 for _ in range(w+1)]for _ in range(n+1)]

#     def ZerosinArray(arr):
#         return len([x for x in arr if x == 0])

#     for i in range(n+1):
#         for j in range(w+1):
#             if i == 0:
#                 dp[i][j] = 0
#             if j == 0:
#                 #  dp[i][j]=1
#                 # if 0 are present in array it will consider only 1 but it should consider {} and 0
#                 dp[i][j] = 2**ZerosinArray(arr[:i])

#     for i in range(1, n+1):
#         for j in range(1, w+1):
#             if arr[i-1] <= j:
#                 dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
#             else:
#                 dp[i][j] = dp[i-1][j]

#     return dp[n][w]


# arr = [2, 3, 5, 6, 8, 10]
# w = 10  # sum
# print(subsetSumCount(len(arr), arr, w))

# arr = [1, 2, 3, 4, 5]
# sum = 10
# n = len(arr)

# print(subsetSumCount(n, arr, sum))


# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # MINIMUM SUBSET SUM DIFFERENCE

# # PROBLEM LINK: https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# def minDifference(arr, n):
#     # code here
#     # def solver(n,w,diff):
#     #     if n==0:
#     #         x=abs(w-(W-w))
#     #         if diff>x:
#     #             diff=x
#     #         return diff

#     #     if arr[n-1]<=w:
#     #         diff= min(solver(n-1,w-arr[n-1],diff), solver(n-1,w,diff))
#     #     else:
#     #         diff= solver(n-1,w,diff)

#     #     return diff

#     # W=sum(arr)
#     # w=W

#     # return solver(n,w,float('inf'))


#     # # Memoization

#     # def solver(n,w,dp):
#     #     if n==0:
#     #         x=abs(w-(W-w))
#     #         if dp[n][w]>x:
#     #             dp[n][w]=x
#     #         return dp[n][w]

#     #     if dp[n][w]!=float('inf'):
#     #         return dp[n][w]

#     #     if arr[n-1]<=w:
#     #         dp[n][w]= min(solver(n-1,w-arr[n-1],dp), solver(n-1,w,dp))
#     #     else:
#     #         dp[n][w]= solver(n-1,w,dp)

#     #     return dp[n][w]

#     # W=sum(arr)
#     # w=W
#     # dp=[[float('inf') for _ in range(w+1)]for _ in range(n+1)]
#     # return solver(n,w,dp)


#     # # # Bottom Up Appraoch:
#     W=sum(arr)
#     w=W
#     dp=[[float('inf') for _ in range(w+1)]for _ in range(n+1)]
#     for i in range(n+1):
#         for j in range(w+1):
#             if i==0:
#                 x=abs(j-(W-j))
#                 if dp[i][j]>x:
#                     dp[i][j]=x

#             elif arr[i-1]<=j:
#                 dp[i][j]= min(dp[i-1][j-arr[i-1]],dp[i-1][j])
#             else:
#                 dp[i][j]=dp[i-1][j]

#     return dp[n][w]

# arr=[1,6,11,5]
# print(minDifference(arr,len(arr)))

# arr=[1,4]
# print(minDifference(arr,len(arr)))
