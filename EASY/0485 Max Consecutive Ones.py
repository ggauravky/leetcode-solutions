# 485. Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

nums =[1,0,1,1,0,1]

count = 0
ans = 0

for num in nums:
    if num == 1:
        ans += 1
        count = max(count, ans)
    else:
        ans= 0

print(count)
