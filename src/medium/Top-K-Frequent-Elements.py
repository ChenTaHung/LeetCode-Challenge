"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k :
            return nums
        
        heap = []
        defdict = defaultdict(int)

        for n in nums:
            defdict[n] += 1
        
        # create a heap to pop out the k most frequent elements
        for i in defdict.items():  # (key, cnt)
            heapq.heappush(heap, i)

        """
        By default, heapq is a min-heap, so we need to pop the smallest elements.
        In this case, we can store the values as (-count, number) to simulate a max-heap.
        """
            
        return [i for i, j in heapq.nlargest(k, heap, key = lambda h: h[1])]
