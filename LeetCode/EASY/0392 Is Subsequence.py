# 392. Is Subsequence
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

s = "axc"
t = "ahbgdc"

for i in s:
    if i in t:
        t = t[t.index(i)+1:]
    else:
        print(False)
        break
else:
    print(True)
