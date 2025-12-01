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
        """
        :type strs: List[str]
        :rtype: str
        """
    
    
strs=["flower", "flow", "flight"]

# print(len(strs))

for i in range(len(strs)-1):
    str1=strs[i]
    str2=strs[i+1]
    list=[]
    list.append(str1)
    list.append(str2)
    val=0
    if len(str1)>len(str2):
        ran=str2
    else:
        ran=str1
    bucket=[]
    for j in range(0,len(ran)):
        if(str1[j]==str2[j]):
            bucket.append(ran[j])
            val=val+1
        else:
            break
    bucket = ''.join(bucket)
    if (len(bucket)<=len(ran)):
        final_str=bucket
    else:
        continue
print(final_str)