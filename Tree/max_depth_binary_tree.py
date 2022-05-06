'''
Difficulty: Easy

https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        Recursive Depth for search
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

    def MaxDepthBFS(self, root):
        # Breadth for search using queue
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1
        return level

    def MaxDepthDFS(self, root):
        # Using stack and depth for search iteratively

        stack = [[root, 1]]
        result = 0
        while stack:
            node, depth = stack.pop()

            if node:
                result = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result
