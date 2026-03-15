# 451. Sort Characters By Frequency
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        result = ""
        
        for ch in sorted(count, key=count.get, reverse=True):
            result += ch * count[ch]
        
        return result

#complexity analysis
# Time complexity: O(n log n), where n is the length of the input string s. This is because we need to sort the characters based on their frequency, which takes O(n log n) time in the worst case.
# Space complexity: O(n), where n is the length of the input string s. This is because we need to store the frequency of each character in a dictionary, which can take up to O(n) space in the worst case if all characters are unique. Additionally, the result string can also take up to O(n) space in the worst case if all characters are unique. 