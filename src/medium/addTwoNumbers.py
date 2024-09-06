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