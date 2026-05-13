# 1952. Three Divisors
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

# An integer m is a divisor of n if there exists an integer k such that n = k * m.

 

# Example 1:

# Input: n = 2
# Output: false
# Explantion: 2 has only two divisors: 1 and 2.
# Example 2:

# Input: n = 4
# Output: true
# Explantion: 4 has three divisors: 1, 2, and 4.

class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                
        return count == 3