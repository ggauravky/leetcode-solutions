# 1781. Sum of Beauty of All Substrings
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

 

# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17


from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        for i in range(n):
            for j in range(i, n):
                sub = s[i:j+1]
                freq = Counter(sub).values()
                ans += max(freq) - min(freq)
                
        return ans