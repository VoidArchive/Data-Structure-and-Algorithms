'''
Difficulty: Easy

https://leetcode.com/problems/maximum-subarray/

Given an integer array nums,
find the contiguous subarray
(containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += n
            max_sub = max(max_sub, curr_sum)

        return max_sub
