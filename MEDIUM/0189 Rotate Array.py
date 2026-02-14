# 189. Rotate Array
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

nums = [1,2,3,4,5,6,7]
k = 3

# for i in range(k+1):
#     print(nums)
#     nums[0]=nums[-1]
#     print("-----")
#     print(nums)
#     nums.pop(-1)
#     print("*********************")

# print(nums)

k %= len(nums)

for _ in range(k):
    last = nums.pop()      # remove last
    nums.insert(0, last)   # insert at front