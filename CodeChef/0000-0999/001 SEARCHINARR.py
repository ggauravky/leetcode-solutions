# Search an element in an array
# You are given an array 
# A
# A of size 
# N
# N and an element 
# X
# X. Your task is to find whether the array 
# A
# A contains the element 
# X
# X or not.

# Function Declaration
# Function Name
# s
# o
# l
# v
# e
# solve – This function checks whether a given element X is present in the array A.

# Parameters
# N
# N : An integer representing the number of elements in the array.
# X
# X : An integer representing the element to be searched.
# A
# A : A list/array of integers of length N, representing the input array.
# Return Value
# Returns a string:

# "YES" if the element 
# X
# X exists in the array 
# A
# A.
# "NO" if the element 
# X
# X is not present in the array.
# Input Format
# The first line contains two space-separated integers 
# N
# N and 
# X
# X — the size of array and the element to be searched.
# The second line contains all the elements of array 
# A
# A
# Output Format
# Output "YES" if the element 
# X
# X is present in 
# A
# A, otherwise output "NO".

# Constraints
# 1
# ≤
# N
# ,
# X
# ≤
# 10
# 5
# 1≤N,X≤10 
# 5
 
# 1
# ≤
# A
# i
# ≤
# 10
# 5
# 1≤A 
# i
# ​
#  ≤10 
# 5

def solve(N, X, A):
    for i in A:
        if i == X:
            return "YES"
    return "NO"