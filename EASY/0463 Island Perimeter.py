# 463. Island Perimeter
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        row=len(grid)
        cols=len(grid[0])
        peri=0

        for i in range(row):
            for j in range(cols):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]==0:
                        peri+=1
                    if i==row-1 or grid[i+1][j]==0:
                        peri+=1
                    if j==0 or grid[i][j-1]==0:
                        peri+=1
                    if j==cols-1 or grid[i][j+1]==0:
                        peri+=1
        return peri

