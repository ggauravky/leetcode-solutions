# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 
nums = [0,1,0,3,12]
ans1=[]
ans2=[]
for i in nums:
    if i !=0:
        ans1.append(i)
    else:
        ans2.append(i)
        
print(ans1)
print(ans2)

print(ans1+ans2)