# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        def common(a, b):
            result = []
            for i in range(min(len(a), len(b))):
                if a[i] == b[i]:
                    result.append(a[i])
                else:
                    break
            return ''.join(result)

        prefix = strs[0]

        for i in range(1, len(strs)):
            prefix = common(prefix, strs[i])
            if prefix == "":
                break

        return prefix

    
    
def longestCommonPrefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]

    # Function to find common prefix between two strings
    def common(a, b):
        result = []
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]:
                result.append(a[i])
            else:
                break
        return ''.join(result)

    prefix = strs[0]

    for i in range(1, len(strs)):
        prefix = common(prefix, strs[i])
        if prefix == "":
            break

    return prefix

longestCommonPrefix(["flower", "flow", "flight"])
longestCommonPrefix(["dog", "racecar", "car"])
