# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepyth(root.left), self.maxDepth(root.right))
