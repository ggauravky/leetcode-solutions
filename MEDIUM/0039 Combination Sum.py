# 39. Combination Sum
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []
 
 
# candidates = [2,3,6,7]
# target = 7
# ans=[]
# temp=0

# for candidate in candidates:
#     for i in range(target):
#         temp=candidate+candidate
#         if temp==target:
#             ans.append(i)
#         if temp>target:
#             break
#         print(temp)
#     temp=0
# print(ans)

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, remaining, path):
            # If target becomes 0, we found a valid combination
            if remaining == 0:
                result.append(path[:])
                return
            
            # Try each number starting from 'start'
            for i in range(start, len(candidates)):
                num = candidates[i]
                
                # If number is bigger than remaining target, skip
                if num > remaining:
                    continue
                
                path.append(num)                         # choose
                backtrack(i, remaining - num, path)      # reuse allowed
                path.pop()                               # backtrack

        backtrack(0, target, [])
        return result
