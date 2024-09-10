"""
9.  Palindrome Number

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return(False)

        str_x = str(x)
        len_x = len(str_x)
        
        if len_x % 2 == 0 :
            cutoff_id = int(len_x / 2)
            former = str_x[:cutoff_id]
            latter = str_x[cutoff_id:]
        else:
            cutoff_id = int(len_x / 2) 
            former = str_x[:cutoff_id]
            latter = str_x[cutoff_id+1:]

        
        if former == latter[::-1] :
            return(True)
        else:
            return(False)
        
        
class Solution:
    """
    not converting to string
    """
    def reverse_integer(self, n: int) -> int:
        reversed_int = 0
        while n > 0:
            reversed_int = reversed_int * 10 + n % 10
            n //= 10

        return reversed_int
                
    def isPalindrome(self, x: int) -> bool:

        if x < 0 :
            return False
        elif x in [*range(10)] : 
            return True
        else:

            n_digit = len(str(x))
            
            if n_digit % 2 == 0:
                divider = 10 ** int(n_digit / 2)
                former = x // divider
                latter = x % divider
            else:
                divider = 10 ** int(n_digit / 2)
                former = x // (divider * 10)
                latter = x % divider
            
            zero_suffix = True
            
            while zero_suffix:
                if former % 10 == 0:
                    former //= 10
                else:
                    zero_suffix = False

            print(former)
            print(latter)

            if int(former) == int(self.reverse_integer(n = latter)) :
                return True
            else:
                return False