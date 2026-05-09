# 1408. String Matching in an Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        ans = []
        
        for i in range(len(words)):
            for j in range(len(words)):
                
                if i != j and words[i] in words[j]:
                    ans.append(words[i])
                    break
                    
        return ans