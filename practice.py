# n binary strings, s1..sn each of length k.
# you have array A of binary strings initiallly empty and binary string T of length K which consists of all zeros initially
# in one operation you can do following 
# choose some indesx i such that 1<=i <=k and change the value at that position  from 0 to 1 or from 1 to 0. in the string T.
# append the string T to the end of A.
# After performing all operations A must contain all of the strings S1..Sn.
#  Find the total number of posiible strings which can be in A after performaing all operations.
# all the given strings are distinct and none of them is equal to the string which contains all zeros.

# Input format, first line contains N denoting number of elements in S.
# next line contains K denoting length of each stirng in S.
# each line of i of the N subsequent lines where 1<i<N contains string describing S[i]

# Constrains:
# 1 < N<=15
# 1<=K<10^4
# k<=lenS[i]<=k

# Input
# 3
# 2
# 01
# 10
# 11

# output: 3

# Explanation: given N=3 and k=2 and S=[["01"], ["10"], ["11"]]
# Initially T=00 and A=[] after first operation T=01, A=["01"]
# after second operation T=11, A=["01", "11"]
# after third operation T=10, A=["01", "11", "10"]
# so final output 3

# Input 2:
# 3
# 3
# 001
# 111
# 100

# output:
# 5
# Explanation: ["001","011","111", "110","100"]

# Input3:
# 4
# 3
# 001
# 111
# 100
# 010

# Ouput:
# 7
# Explanation: ["001","011","111", "110","100","110", "010"]

from collections import deque
def solve():
    # Input reading
    N = int(input())  # number of strings
    K = int(input())  # length of each string
    strings = [input().strip() for _ in range(N)]  # list of N strings
    
    # Set to track required strings to generate
    required_strings = set(strings)
    
    # BFS setup to find all possible strings starting from '00..0'
    initial_T = '0' * K
    queue = deque([initial_T])  # queue for BFS
    visited = set([initial_T])  # track visited states to avoid duplicates
    generated = set([initial_T])  # track generated distinct strings
    
    while queue:
        current = queue.popleft()
        
        # If we've generated all required strings, we can stop
        if required_strings.issubset(generated):
            break
        
        # Try flipping each bit to generate new strings
        for i in range(K):
            # Flip the ith bit
            flipped = current[:i] + ('1' if current[i] == '0' else '0') + current[i+1:]
            
            if flipped not in visited:
                visited.add(flipped)
                queue.append(flipped)
                generated.add(flipped)
    
    # Return the number of distinct strings, excluding the initial all-zero string
    generated.discard(initial_T)
    print(len(generated))

# Example usage:
print(solve())
