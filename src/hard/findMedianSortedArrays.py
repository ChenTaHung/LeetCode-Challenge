"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def mergeSort(l1: List[int], l2: List[int]) -> List:
            L = l1 + l2
            L.sort()
            return(L)

        mergeArr = mergeSort(nums1, nums2)
        
        if len(mergeArr) == 1 :
            return(mergeArr[0])
        else:
            if len(mergeArr) % 2 == 0 : #even
                sel_id = int(len(mergeArr) / 2) - 1

                return((mergeArr[sel_id] + mergeArr[sel_id + 1]) / 2)
            else: # odd number
                sel_id = int(len(mergeArr) / 2 - 1)

                return(mergeArr[sel_id+1])

