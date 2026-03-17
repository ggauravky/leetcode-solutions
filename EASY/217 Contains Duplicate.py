# 17. Contains Duplicate
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    

#` Complexity Analysis
# Time Complexity: O(n), where n is the length of the input array nums. We  traverse the array once to create a set of unique elements, which takes O(n) time.
# Space Complexity: O(n), in the worst case, if all elements in the array are distinct, the set will contain all n elements, resulting in O(n) space complexity.    