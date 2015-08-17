# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root

    # DFS
    def invertTree2(self, root):
    	stack = [root]
    	while stack:
    		node = stack.pop()
    		if node:
    			node.left, node.right = node.right, node.left
    			stack.extend([node.left, node.right])

    def invertTree3(self, root):
    	queue = [root]
    	while queue:
    		node = queue.pop(0)
    		if node:
    			node.left, node.right = node.right, node.left
    			queue.append(node.left)
    			queue.append(node.right)
    	return root