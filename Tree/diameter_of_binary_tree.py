'''
Difficulty: Easy
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
 This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = [0]

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]

        
        