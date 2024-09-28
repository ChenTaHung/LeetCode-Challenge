"""
84. Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = []
        max_area = 0
        prev_idx = None

        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]: # next height is smaller than previous
                prev_idx = stack[-1][0] # get the previous index for the next push, the farest previous index that can reach by current height backward
                width = i - prev_idx 
                height = stack[-1][1]
                max_area = max(max_area, width * height)
                stack.pop()
                

            if prev_idx is not None:
                stack.append((prev_idx, h))
                prev_idx = None
            else:
                stack.append((i, h)) 
        
        while stack : # the remaining stack will need to compare from their position to the end of the histogram, and see if the underground area is greater than maximum or not.
            width = length - stack[-1][0]
            height = stack[-1][1]
            max_area = max(max_area, width * height)
            stack.pop()
        
        return max_area

            
