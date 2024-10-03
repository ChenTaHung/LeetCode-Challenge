"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring
 without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        left = 0
        right = 1
        hashtable = defaultdict(int)
        hashtable[s[left]] += 1
        max_len = 0

        while right < len(s) and left < len(s):

            if hashtable.get(s[right], 0) != 0 : # repeated string encounter
                hashtable[s[left]] -= 1
                left += 1
            else:
                hashtable[s[right]] += 1
                right += 1

            max_len = max(max_len, right - left)
        
        return max_len
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        len_s = len(s)
        
        longest_len = 0
        
        for i in range(len(s)): 
            lenght = 0 # init

            archor = s[i]
            j = 0
            while i+j+1 < len_s:
                new_chr = s[i+j+1]
                if new_chr in archor:
                    break
                else:
                    archor += new_chr
                    j += 1

            if len(archor) > longest_len :
                longest_len = len(archor)
        

        return(longest_len)