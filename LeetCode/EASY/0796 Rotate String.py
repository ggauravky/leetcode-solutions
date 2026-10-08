# 796. Rotate String
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false
 
 
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        # Step 1: lengths must be same
        if len(s) != len(goal):
            return False
        
        # Step 2: concatenate s with itself
        doubled = s + s
        
        # Step 3: check if goal is substring
        if goal in doubled:
            return True
        
        return False