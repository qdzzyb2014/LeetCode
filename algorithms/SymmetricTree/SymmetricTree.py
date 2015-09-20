# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
        	return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if left and right and left.val == right.val:
        	return self.helper(left.right, right.left) and self.helper(left.left, right.right)

        return left == right

    def isSymmetric(self, root):
        if not root:
            return True
        stack = [(root.right, root.left)]
        while stack:
            right, left = stack.pop(0)
            if not right and not left:
                continue
            if not right or not left:
                return False
            if right.val == left.val:
                stack.append((right.right, left.left))
                stack.append((right.left, left.right))
            else:
                return False
        return True