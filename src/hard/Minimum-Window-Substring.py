"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t :
            return t
        
        if len(t) > len(s) :
            return ""
        
        tArr = [0] * 58
        
        needMatchCnt = 0
        for i in t:
            idx = ord(i) - ord('A')
            tArr[idx] += 1
            needMatchCnt += 1
        
        left, right = 0, 0
        dist = [(left, right), float('inf')]
        
        while left < len(s) :
            
            if needMatchCnt > 0 and right < len(s):
                idxR = ord(s[right]) - ord('A')
                if tArr[idxR] > 0: # appear in t
                    needMatchCnt -= 1
                
                tArr[idxR] -= 1
                right += 1 # expand window
            else:
                idxL = ord(s[left]) - ord('A')
                if needMatchCnt == 0 : # range cover all characters in t, we can start shift left to shrink windows
                    
                    if dist[1] > right - left : # a shorter substring
                        dist = [(left, right), right - left] # update
                
                if tArr[idxL] >= 0 : # appear in t
                    needMatchCnt += 1 # reset the count
                    
                tArr[idxL] += 1 # we need to find this character again
                left += 1
        
        return "" if dist[1] == float('inf') else s[dist[0][0]: dist[0][1]]
                    
            
            
            