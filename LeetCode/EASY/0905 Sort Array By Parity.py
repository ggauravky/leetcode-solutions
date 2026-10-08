# 905. Sort Array By Parity

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]

nums = [0]
temp=[]

for num in nums:
    if(num%2==0):
        temp.append(num)
        
for num in nums:
    if(num%2!=0):
        temp.append(num)

print(temp)

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=[]

        for num in nums:
            if(num%2==0):
                temp.append(num)
        
        for num in nums:
            if(num%2!=0):
                temp.append(num)
        return temp