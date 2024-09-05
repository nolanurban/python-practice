# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

nums = [ 1, 2, 3, 4, 5 ]
target = 9

output = []

left = 0
right = left + 1

# create a while loop that will work 0 -> [ rest of the array ] and then increment
target_met = False

while (True):
    print(f"left: {left} right: {right}")
    if nums[left] + nums[right] == target:
        print("FOUND")
        break
    if right == len(nums) - 1:
        left += 1
        right = left + 1
        continue
    if left == len(nums): target_met == True
    right += 1


list_return = [ left, right ]
print(list_return)

# 1 2 3 4 5
# 1 2
# 1 3
# 1 4
# 1 5
# 2 3
# 2 4
# 2 5
# 3 4
# 3 5
# 4 5
