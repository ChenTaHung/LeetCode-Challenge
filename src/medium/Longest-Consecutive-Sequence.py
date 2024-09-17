"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_nums = sorted(nums) # it is not O(n) anymore
        
        if not nums: # empty list
            return 0
            
        i = 1
        consecSeq = 1
        consecSeqList = []

        while i < len(sort_nums) :
            
            while i != len(sort_nums) - 1 and sort_nums[i-1] == sort_nums[i]: # repeated same number
                i += 1 # ignore and go next
                
            if sort_nums[i] - sort_nums[i - 1] == 1: # if consecutive
                consecSeq += 1
            else:
                consecSeqList.append(consecSeq) # store the consecutive count "so far"
                consecSeq = 1
            
            i += 1

        
        if not consecSeqList : # the entire list is consecutive
            return consecSeq
        else:
            consecSeqList.append(consecSeq) # store the last count of consecutive number
            return max(consecSeqList) # return the maximum
        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        streak = 0

        for num in nums_set:

            if num - 1 not in nums_set: # it is a start
                start = num
                consecutive = 1        
                
                while start + 1 in nums_set:
                    consecutive += 1
                    start += 1
                
                streak = max(streak, consecutive)


        return streak