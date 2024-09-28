"""
74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            mid = len(arr)  // 2
            min_ = 0
            max_ = len(arr) - 1
            
            if arr[max_] < target:
                continue
            else:
                while arr[mid] != target:
                    if arr[mid] > target:  # min_   target  mid
                        max_ = mid - 1
                    else:
                        min_ = mid + 1
                    
                    if mid == (max_ + min_) // 2 :
                        return False
                    else:
                        mid = (max_ + min_) // 2
            
                return True

                