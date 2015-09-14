# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
    	pre, pre.next = self, head
    	while pre.next and pre.next.next:
    		a = pre.next
    		b = a.next
    		pre.next, b.next, a.next = b, a, b.next
    		pre = a
    	return self.next