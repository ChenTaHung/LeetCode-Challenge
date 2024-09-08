"""
5. Longest Palindromic Substring
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        
        for l in range(len_s, 0, -1): # length of substring
            if l % 2 == 0: # length of substring is even
                j = 0
                while j + l <= len_s:
                    subs = s[j:j+l] # fixed window text extraction
                    
                    cutoff_id = int(l / 2)
                    former_part = subs[:cutoff_id]
                    latter_part = subs[cutoff_id:]
                
                    if former_part == latter_part[::-1]:
                        return(subs)
                    else: 
                        j += 1

            else: # length of substring is odds
                j = 0
                while j + l <= len_s:
                    subs = s[j:j+l] # fixed window text extraction
                    
                    cutoff_id = int(l / 2)
                    former_part = subs[:cutoff_id]
                    latter_part = subs[cutoff_id+1:]
                
                    if former_part == latter_part[::-1]:
                        return(subs)
                    else: 
                        j += 1
                        