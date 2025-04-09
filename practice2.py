# you are given sting s whihc consist of lowercase latin letters ['a','b','c',.....,'z]
# cost of string is defained as sum of absolute differences of ASCII values of all possibe pairs of characters present in S
# find total cost of S
# the pari with indices (i,j) and (j,i) is considered same pair

# input: "aaaaa"
# ouput : 0

# since there is only one unique character there are no paris to compute so cost of string S is 0

# input:
# aabbcc
# output:
# 16
# ascii values for a, b, c are 97,98,99
# total cost of difference between thm is 4*[abs(97-98)] + 4*[abs(97-99)] + 4*[abs(98-99)] =16

# input
# abcde
# output
# 20
from collections import Counter
def calculate_string_cost(s):
    freq = Counter(s)
    chars = list(freq.keys())
    cost = 0
    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            char1, char2 = chars[i], chars[j]
            ascii_diff = abs(ord(char1) - ord(char2))
            pair_cost = freq[char1] * freq[char2] * ascii_diff
            cost += pair_cost
    
    return cost

# Example usage:
s = "aaaaa"
print(calculate_string_cost(s))
s = "abcde"
print(calculate_string_cost(s))
s = "aabbcc"
print(calculate_string_cost(s))
