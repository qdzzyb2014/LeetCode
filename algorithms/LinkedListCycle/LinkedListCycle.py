# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle1(self, head):
        try:
            slow = head
            fast = head.next
            while slow in not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

    def hasCycle2(self, head):
        if not head:
            return False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fasl.next.next
            if slow == fast:
                return True
        return False
