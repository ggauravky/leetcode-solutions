# 219. Contains Duplicate II
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in seen:
                prev_index = seen[num]
                if i - prev_index <= k:
                    return True

            seen[num] = i

        return False

# Complexity Analysis
# Time Complexity: O(n), where n is the length of the input array nums. We traverse the array once.
# Space Complexity: O(n), in the worst case, we may store all elements of the array in the seen dictionary if all elements are distinct.
