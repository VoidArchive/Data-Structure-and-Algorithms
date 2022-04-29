'''
Difficulty: Easy

https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        Brute force solution: Time: O(n^2)  Space: O(1)
        Checking if the item in array is already in a list, if there is then it contains duplicate.
        if not add the item to that list.
        
        """
        a = []
        for i in nums:
            if i in a:
                return True
            a.append(i)
        return False
        
    def containsDuplicate_hashset(self, nums):
        """
        Using hashset: Time: O(n) Space: 0(n)
        Sets are implemented using hash tables that means whenever we add an object to a set,
        the position within the memory of the set object is determined using the hash of the object to be added.
        A downside of this method is it uses more memory but is a lot faster that Brute forcing. 

        """
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False