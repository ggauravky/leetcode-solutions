# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of multiple lines of input.
# The first line of each test case contains a single integer 
# N
# N - the size of the array.
# The next line of each test case contains 
# N
# N space-separated integers 
# A
# 1
# ,
# A
# 2
# ,
# …
# ,
# A
# N
# A 
# 1
# ​
#  ,A 
# 2
# ​
#  ,…,A 
# N
# ​
#   - the elements of the array.
# Output Format
# For each test case, output on a new line, the minimum number of operations required to make 
# M
# M the maximum value in the array 
# A
# A.

# Constraints
# 1
# ≤
# T
# ≤
# 100
# 1≤T≤100
# 1
# ≤
# N
# ≤
# 100
# 1≤N≤100
# 1
# ≤
# A
# i
# ≤
# 100
# 1≤A 
# i
# ​
#  ≤100
# Sample 1:
# Input
# Output
# 3
# 2
# 1 2
# 4
# 2 2 3 4
# 1
# 1
# 1
# 2
# # 0


class Solution:
    def count_non_minimum(self, nums):
        minimum = min(nums)
        return sum(1 for num in nums if num > minimum)
    


class Solution:
    def count_non_minimum(self, nums):
        minimum = min(nums)
        count = 0

        for num in nums:
            if num > minimum:
                count += 1

        return count