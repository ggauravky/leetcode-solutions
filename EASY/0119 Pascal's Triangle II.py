# 119. Pascal's Triangle II
# recheck
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 
 
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]  # The first row (0th index) of Pascal's Triangle
        for _ in range(rowIndex):
            # Generate the next row using the current row
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row
