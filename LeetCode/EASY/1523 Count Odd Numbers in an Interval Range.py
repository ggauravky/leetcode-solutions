# 1523. Count Odd Numbers in an Interval Range

# Hint
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:

# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].

low = 3
high = 7
count=0

for i in range(low, high+1):
    if i%2!=0:
        count=count+1

print(count)    

#above code will reach memory , when a long list or array is there

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high - low) // 2 + (1 if low % 2 == 1 or high % 2 == 1 else 0)