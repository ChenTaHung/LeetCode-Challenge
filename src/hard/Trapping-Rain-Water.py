"""
42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2 :
            return 0
        
        left = 0
        right = len(height) - 1
        
        max_left = height[left]
        max_right = height[right]
        
        container = 0
        while left < right: # pointers do not overlap
            
            if max_left <= max_right: # We know that there is a higher bar at rhs, so calculate rain trapped from lhs

                if max_left - height[left] > 0:
                    container += (max_left - height[left])
                left += 1

                if height[left] > max_left :
                    max_left = height[left] # update max lhs bar

            else: # higher lhs bar, so calculate rain trapped from rhs

                if max_right - height[right] > 0:
                    container += (max_right - height[right])
                right -= 1

                if height[right] > max_right :
                    max_right = height[right] # update max rhs bar

        return container    
    
class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2:
            return 0
        
        container = 0

        i = 1
        left_limit = 0
        while i < len(height) - 1 :
            
            bottom = height[i]
            
            leftPointer = left  = i - 1
            rightPointer = right = i + 1
            
            if height[leftPointer] > bottom and height[rightPointer] >= bottom : # can create a container
                
                while leftPointer - 1 >= 0 :
                    
                    if leftPointer < left_limit : # do not count a prvious container
                        break
                    
                    # find the highest bar at lhs
                    if height[leftPointer - 1] > height[left]: # found a higher bar
                        left  = leftPointer - 1 # update the left index
                    leftPointer -= 1
                    
                
                while rightPointer + 1 < len(height) :
                    # find the highest bar at rhs
                    if height[rightPointer + 1] > height[right] and height[left] >= height[right] : # found a higher bar
                        right = rightPointer + 1 # update the right index
                    rightPointer += 1
                

                bar_height = min(height[left], height[right])
                # print(left, i, right)
                for j in range(left+1, right) : 
                    if bar_height - height[j] > 0:
                        container += (bar_height - height[j]) 
                
                i = right
                left_limit = right # update the limit point for the left bar
            else:                    
                i += 1
            
        return container
            