# 7. Reverse Integer
# Medium
# Topics
# premium lock icon
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

x = 123
x=str(x)
print(x[::-1])
x=int(x)
print(x)
print(type(x))

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = str(abs(x))
        x = x[::-1]
        result = sign * int(x)

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result
