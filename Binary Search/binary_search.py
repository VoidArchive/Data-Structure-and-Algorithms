'''
Difficulty: Easy
https://leetcode.com/problems/binary-search/


    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
    
Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
    '''


class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1