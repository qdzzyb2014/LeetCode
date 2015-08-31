# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
    	res = cur = ListNode(0)
    	while li and l2:
    		if l1.val < l2.val:
    			cur.next = l1
    			l1 = l1.next
    		else:
    			cur.next = l2
    			l2 = l2.next
    		cur = cur.next
    	cur.next = l1 or l2
    	return res.next