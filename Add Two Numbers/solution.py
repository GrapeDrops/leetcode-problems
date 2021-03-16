# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy_node = ListNode()
        curr_node = dummy_node
        
        while l1 or l2:
            num1, num2 = 0, 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next
            digit = num1 + num2 + carry
            curr_node.next = ListNode(digit % 10)
            curr_node = curr_node.next
            carry = 1 if digit > 9 else 0
            
        if carry:
            curr_node.next = ListNode(1)
            
        return dummy_node.next
