# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution
# Example:
#     Given nums = [2, 7, 11, 15], target = 26,
#     Because nums[2] + nums[3] = 11 + 15 = 26,
#     return [2, 3].

# Solution 1
# Try all 
input_array = [2, 7, 11, 15]
target = 26
result = []
for i, num in enumerate(input_array):
    for j in range(i+1, len(input_array)):
        print(i,j)