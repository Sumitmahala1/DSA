# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values from the two lists
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add the digits and carry
            total = val1 + val2 + carry

            # Current digit
            digit = total % 10

            # New carry
            carry = total // 10

            # Create a new node
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
        