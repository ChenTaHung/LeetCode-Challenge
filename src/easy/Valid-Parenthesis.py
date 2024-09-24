"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        for i in s:
            # print(stack)
            if i in ['(', '[', '{'] : #opening
                stack.append(i)
            else: # closing
                if stack: # at least a opening stored
                    if i == ')' :
                        if stack[-1] == '(' :
                            stack.pop()
                        else:
                            stack.append(i)
                    elif i == ']' :
                        if stack[-1] == '[' :
                            stack.pop()
                        else:
                            stack.append(i)
                    else:
                        if stack [-1] == '{' :
                            stack.pop()
                        else:
                            stack.append(i)
                else: # encounter closing first
                    return False 

        if stack:
            return False
        else:
            return True