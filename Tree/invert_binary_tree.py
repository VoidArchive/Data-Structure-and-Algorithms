'''
Difficulty: Easy
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if root:
            left = root.left
            right = root.right
            
            root.left = right
            root.right = left

            self.invertTree(left)
            self.invertTree(right)
        
        return root