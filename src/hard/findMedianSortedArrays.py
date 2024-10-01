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
        len1 = len(nums1)
        len2 = len(nums2)
        med_len = (len1 + len2) // 2
        
        if (len1 + len2) % 2 == 0 :
            even = True
        else:
            even = False
        
        if len1 <= len2:
            short_, long_ = nums1, nums2
        else:
            short_, long_ = nums2, nums1

        left = 0
        right = len(short_) - 1

        while True :
            mid = (left + right) // 2   
            remain = med_len - (mid + 1) - 1 # if need 6 elements, if mid = 2 means three elements are chosen thus remain element index = 2 (6-2-2)
            
            short_sel = short_[mid] if mid >= 0 else float('-inf')
            short_next = short_[mid + 1] if mid + 1 < len(short_) else float('inf')

            long_sel = long_[remain] if remain >= 0 else float('-inf')
            long_next = long_[remain + 1] if remain + 1 < len(long_) else float('inf')

            if short_sel <= long_next and long_sel <= short_next :
                return (max(short_sel, long_sel) + min(short_next, long_next)) / 2 if even else min(short_next, long_next)
            else:

                if short_sel > long_next :
                    right = mid  - 1
                else:
                    left = mid + 1
            


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

