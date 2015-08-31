# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal1(self, root):
    	res = []
    	self.helper(root, res)

    def helper(self, root, res):
    	if root:
    		self.helper(root.left, res)
    		self.helper(root.right, res)
    		res.append(root.val

    def postorderTraversal(self, root):
    	stack = [root]
    	res = []
    	while stack:
    		node = stack.pop()
    		if node:
    			res.append(node.val)
    			stack.append(node.left)
    			stack.append(node.right)
    	return res[::-1]

    def postorderTraversal(self, root):
    	res, stack = [], [(root, False)]
    	while stack:
    		node, visited = stack.pop()
    		if node:
    			if visited:
    				res.append(node.val)
    			else:
    				stack.append((node, True))
    				stack.append((node.right, False))
    				stack.append((node.left, False))

    	return res
