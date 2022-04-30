'''
Difficulty: Easy
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        Using hashmap, to store the value and index, we can check if difference between target in nums[i] is in the hashmap.
        """
        hashmap = {} # number:index

        for i, number in enumerate(nums):  # Enumerate returns index and value of the list.
            diff = target - number
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[number] = i
        
        return None

