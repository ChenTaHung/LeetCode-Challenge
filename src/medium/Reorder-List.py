"""
143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything; modify head in-place instead.
        """
        if not head or not head.next:
            return

        num_head = 1
        cur = head
        while cur.next:
            num_head += 1  
            cur = cur.next

        mid = num_head // 2 

        # split the list into two halves
        l = 0  # cursor
        cur = head
        prev = None
        while l <= mid:
            prev = cur
            cur = cur.next
            l += 1
        prev.next = None  # break the first half from the second half
        tail = cur  # Start of the second half
        
        # reverse the second half
        def rev_list(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        rev_tail = rev_list(tail)

        # Step 4: Merge the two halves alternately
        h = head  # Cursor for the first half
        t = rev_tail  # Cursor for the reversed second half
        print(h)
        print(t)
        while h and t:
            # save temp var
            h_next = h.next  
            t_next = t.next  

            h.next = t  # Link current node of first half to current node of second half
            if h_next:  # next node in first half exists
                t.next = h_next  # Link current node of second half to next node of first half
            else:
                t.next = None  # End the list if no more nodes in first half

            h = h_next  # Move to next node in first half
            t = t_next  # Move to next node in second half