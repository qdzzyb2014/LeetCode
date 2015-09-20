# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
        	return True
        return abs(self.high(root.right) - self.high(root.left)) <= 1 and
        	self.isBalanced(root.right) and self.isBalanced(root.left)

    def high(self, node):
    	if not node:
    		return 0
    	return 1 + max(self.high(node.right), self.high(node.left))

    # DFS
    def isBalanced(self, root):
    	stack = [root]
    	while stack:
    		cur = stack.pop()
    		if cur:
    			if abs(self.high(root.right) - self.high(root.left)) > 1:
    				return False
    			if cur.right:
    				stack.append(cur.right)
    			if cur.left:
    				stack.append(cur.left)
    	return True