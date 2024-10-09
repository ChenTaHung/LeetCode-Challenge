"""
239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums) :
            return [max(nums)]
        
        deQ = deque([])
        left = 0
        right = 0 
        ans = []
        
        while right < len(nums) :

            while deQ and nums[right] > deQ[-1][1]: # if next item is greater than the previous one, pop it to make the deque descending
                deQ.pop()
            
            deQ.append((right, nums[right]))

            if right - left >= k - 1 : # window range reached
                ans.append(deQ[0][1]) # the left most position store the maximum value
                
                if left == deQ[0][0] :
                    deQ.popleft() # if the left index move over the index of the current stored maximum value, remove it

                left += 1
            
            right += 1

        return ans
            