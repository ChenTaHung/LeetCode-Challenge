"""
Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # create array to store the value:
        len_s = len(s)
        if numRows >= len_s:
            return(s)
        
        L = []

        # init the first col for `numRows` rows
        for r in range(0, numRows):
            L.append(list(s[r]))
        
        # if 4: [2,1,0,1,2,3]
        # if 5: [3,2,1,0,1,2,3,4]
        
        order_list = [*range(numRows - 2, 0, -1)] + [*range(numRows)]
        
        len_order = len(order_list)

        for i, c in enumerate(s[numRows:]):
            order = order_list[((i+1) % len_order) - 1]
            L[order].append(c)
        
        ret = ''
        for r in range(0, numRows):
            ret = ret + ''.join(L[r])

        return(ret)