# 1614. Maximum Nesting Depth of the Parentheses
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:

# Input: s = "(1)+((2))+(((3)))"

# Output: 3

# Explanation:

# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:

# Input: s = "()(())((()()))"

# Output: 3


class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0
        
        for ch in s:
            if ch == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif ch == ')':
                current_depth -= 1
                
        return max_depth