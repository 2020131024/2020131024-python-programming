# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # odd
        if fast is not None:
            slow = slow.next

        fast = head

        last = None
        while slow:
            _next = slow.next
            slow.next = last
            last = slow
            slow = _next
        slow = last

        while slow and fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next

        return True
