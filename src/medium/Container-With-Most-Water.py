"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104


"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        lhs = 0
        rhs = len(height) - 1
        
        ref_contain = 0

        while lhs < rhs :
            new_contain = min(height[lhs], height[rhs]) * (rhs - lhs)
            
            if new_contain > ref_contain :
                ref_contain = new_contain

            if height[lhs] > height[rhs] :
                rhs -= 1
            else:
                lhs += 1

        return ref_contain


        # sort_height = sorted(list(set(height)), reverse = True) # remove duplicate, we only need values start from the maximum
        # len_height = len(sort_height)
        # ref_contain = 0

        # for i in range(len_height) : # index to select the top height
            
        #     sel_h = sort_height[i]
        #     id_list = [i for i, j in enumerate(height) if j == sel_h] # id that match the selected height

        #     if len(id_list) == 1: # only match once
        #         if i != (len_height - 1) :
        #             j = i+1
        #             next_max_height = sort_height[j]
        #             height[id_list[0]] = next_max_height # replace the value with the second highest height
        #     else: # if we match more than two, take the largest range in the index difference

        #         cal_length = max(id_list) - min(id_list)

        #         new_contain = sel_h * cal_length
        #         if new_contain > ref_contain:
        #             ref_contain = new_contain
                
        #         if i != (len_height - 1) :
        #             j = i+1
        #             next_max_height = sort_height[j]
        #             for k in id_list:
        #                 height[k] = next_max_height # replace the value with the second highest height


        # return ref_contain

                        