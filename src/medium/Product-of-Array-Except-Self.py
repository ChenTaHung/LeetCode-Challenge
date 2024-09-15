"""
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        len_n = len(nums)
        ret_ans = [1] * len_n
        
        prefix = 1
        for i in range(len_n):
            ret_ans[i] = prefix # ignore value in the first round 
            prefix *= nums[i] # update prefix with product for next loop to insert into `ret_ans`
        
        suffix = 1
        for i in range(len_n-1, -1, -1):
            ret_ans[i] *= suffix # ignore value in the first round 
            suffix *= nums[i] # update suffix with product for next loop to insert into `ret_ans`
        
        return ret_ans

        # len_n = len(nums)

        # prefix = [1] * len_n
        # suffix = [1] * len_n
        # ret_ans = [0] * len_n

        # for i in range(len_n):
        #     n = nums[i]
        #     if i == 0 :
        #         prefix[i] = n
        #     else:
        #         prefix[i] = prefix[i - 1] * n

        # for i in range(len_n-1, -1, -1):
        #     n = nums[i]
        #     if i == (len_n-1) :
        #         suffix[i] = n
        #     else:
        #         suffix[i] = suffix[i + 1] * n
        

        # ret_ans[0] = suffix[1]
        # ret_ans[len_n - 1] = prefix[len_n - 2]
        # i = 1

        # while i < len_n - 1 :
        #     ret_ans[i] = prefix[i-1] * suffix[i+1]
        #     i += 1
        
        # return ret_ans
            