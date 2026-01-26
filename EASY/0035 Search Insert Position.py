# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# nums = [1,3,5,6] 
# target = 5

# nums = [-5, -2, 0, 3, 9]
# target = 3


# def searchInsert(self, nums, target):
#     for i in range(len(nums)):
#         if nums[i] >= target:
#             return i
#     return len(nums)
            
        

# a=searchInsert(nums,target)
# print(a)









nums = [1,3,5,6]
target = 5

for i in range(len(nums)):
    if nums[i] >= target:
        print(i)
        break
