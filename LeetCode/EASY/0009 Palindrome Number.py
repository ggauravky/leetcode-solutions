# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


y=12321


def checkPalindrome(num):
    if num <=0:
        print("num is 0 or -ve")
        return -1
    y=str(num)
    if y==y[::-1]:
        print("yes , it is")
    else:
        print("no")


check=checkPalindrome(y)

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        rev = s[::-1]
        if s == rev:
            return True
        else:
            return False
