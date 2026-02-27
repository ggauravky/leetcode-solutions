# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
        

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result=[]
        for digit in digits:
            letters = phone_map[digit]
            if not result:
                result = list(letters)
            else:
                temp = []
                for combination in result:
                    for letter in letters:
                        temp.append(combination + letter)
                result = temp
        
        return result
    
# Time Complexity: O(3^N * 4^M) where N is the number of digits that map to 3 letters and M is the number of digits that map to 4 letters.
# Space Complexity: O(3^N * 4^M) for storing the combinations
