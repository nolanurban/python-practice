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

nums = [ 2, 7, 5, 11, 15 ] # adjust the array
target = 26 # adjust the target

# we are goi g to work on this as a hashmap solution based off the example given after finding my window approach 
# was mostly inefficient

hash_map_storage = {} # create an blank hashmap to store a (K,V) of (numbers in array, positions in array)

for i in range(len(nums)): # this is the c loop in python
    difference_complement = target - nums[i] 
    print(f"currently checking: {target} - {nums[i]} = {difference_complement}")
    # if we run across the complement in the difference as a KEY, lets alert us with an extra print
    if difference_complement in hash_map_storage: 
        print(f"eureka! -- the location in the array should be [{hash_map_storage.get(difference_complement)}, {i}]")
    hash_map_storage[nums[i]] = i # this will store our hashmap with the values and positions


