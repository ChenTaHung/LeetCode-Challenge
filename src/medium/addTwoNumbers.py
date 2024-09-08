"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 5 -> 6 -> 4
 7 -> 0 -> 8

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_num = 0
        l2_num = 0

        # l1 
        i = 0
        while l1.val is not None:
            l1_num += l1.val * (10 ** i)
            if l1.next is None:
                break
            else:
                l1 = l1.next
                i += 1

        # l2
        j = 0
        while l2.val is not None:
            l2_num += l2.val * (10**j)
            if l2.next is None:
                break
            else:
                l2 = l2.next
                j += 1

        # sumup 
        total = l1_num + l2_num

        str_total = str(total)

        for i, n in enumerate(str_total):
            if i == 0: # first round = last node
                cur = ListNode(val = int(n))
                continue
            else:
                pre = ListNode(val = int(n))
                pre.next = cur
                cur = pre
        
        return(cur)