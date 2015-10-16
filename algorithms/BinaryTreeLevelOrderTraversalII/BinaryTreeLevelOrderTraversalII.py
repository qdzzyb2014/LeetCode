# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, currentlevel, nextlevel = [], [root], []
        while currentlevel:
            res.append([x.val for x in currentlevel if x])
            for node in currentlevel:
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            currentlevel, nextlevel = nextlevel, []
        return res[::-1]
