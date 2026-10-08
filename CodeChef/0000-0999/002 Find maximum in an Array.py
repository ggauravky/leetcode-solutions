# Find maximum in an Array
# Given a list of 
# N
# N integers, representing height of mountains. Find the height of the tallest mountain.

# Input:
# First line will contain 
# T
# T, number of testcases. Then the testcases follow.
# The first line in each testcase contains one integer, 
# N
# N.
# The following line contains 
# N
# N space separated integers: the height of each mountains.
# Output:
# For each testcase, output one line with one integer: the height of the tallest mountain for that test case.

# Constraints
# 1
# ≤
# T
# ≤
# 10
# 1≤T≤10
# 1
# ≤
# N
# ≤
# 100000
# 1≤N≤100000
# 0
# ≤
# 0≤ height of each mountain 
# ≤
# 10
# 9
# ≤10 
# 9



T = int(input())

for _ in range(T):
    N = int(input())

    arr = []

    numbers = input().split()

    for num in numbers:
        arr.append(int(num))

    print(max(arr))
