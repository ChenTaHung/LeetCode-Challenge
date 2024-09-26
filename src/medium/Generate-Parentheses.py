"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        ans = []

        def bt(leftN, rightN) :
            if leftN == rightN == n :
                ans.append(''.join(stack))
                return ans

            if leftN < n :
                stack.append('(')
                bt(leftN +1, rightN)
                stack.pop()
                
            if leftN > rightN :
                stack.append(')')
                bt(leftN, rightN + 1)
                stack.pop()
                

        bt(0, 0)
        return ans