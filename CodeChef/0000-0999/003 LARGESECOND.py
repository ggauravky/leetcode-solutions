# Largest and Second Largest
# You are given an array 
# A
# A of 
# N
# N integers.
# Find the maximum sum of two distinct integers in the array.

# Note: It is guaranteed that there exist at least two distinct integers in the array.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of multiple lines of input.
# The first line of each test case contains single integer 
# N
# N — the size of the array.
# The next line contains 
# N
# N space-separated integers, denoting the array 
# A
# A.
# Output Format
# For each test case, output on a new line, the maximum sum of two distinct integers in the array.

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 2
# ≤
# N
# ≤
# 10
# 5
# 2≤N≤10 
# 5
 
# 1
# ≤
# A
# i
# ≤
# 1000
# 1≤A 
# i
# ​
#  ≤1000
# The sum of 
# N
# N over all test cases does not exceed 
# 2
# ⋅
# 10
# 5
# 2⋅10 
# 5
#  .


A = [4, 1, 6, 3]
print(max(A) + sorted(A, reverse=True)[1])

second_greatest = sorted(A, reverse=True)[:2]
print(second_greatest[0] + second_greatest[1])

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1

    second_greatest = sorted(set(a), reverse=True)[:2]

    print(second_greatest[0] + second_greatest[1])