"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        Deq = deque([root])
        res = []

        while Deq :
            level_list = []
            
            for _ in range(len(Deq)): # same list will be in the Deque at the same time
            
                node = Deq.popleft()

                if node:
                    level_list.append(node.val)

                # All the child nodes will be append into the Deq for the next for loop
                if node.left:
                    Deq.append(node.left) 

                if node.right:
                    Deq.append(node.right)
            
            res.append(level_list)

        return res            

        