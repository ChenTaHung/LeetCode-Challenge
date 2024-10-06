"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ns = len(s)
        maxlen = 0

        for i in range(ord('A'), ord('Z')+1) : # loop through all upper letter
            c = chr(i)
            left, right, tmpk = 0, 0, k

            while right < ns:

                if s[right] == c:
                    right += 1
                elif tmpk > 0 : # able to replace

                    tmpk -= 1 # replace
                    right += 1
                else: # not able to replace anymore
                    if s[left] != c :  # pass the one that right index has replaced before
                        tmpk += 1
                    
                    left += 1
            
                maxlen = max(maxlen, right - left)
        
        return maxlen