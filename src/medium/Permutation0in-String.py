"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2 :
            return True
        # init array
        strArr = [0] * 150
        
        for c in s1:
            strArr[ord(c)] += 1

        left = 0
        right = 1

        while right < len(s2) and right < len(s2) :

            strArrIter = strArr.copy()

            if strArrIter[ord(s2[left])] > 0 : # appear in s1
                strArrIter[ord(s2[left])] -= 1
                while right < len(s2) :

                    if strArrIter[ord(s2[right])] > 0 : # next character is in s1
                        strArrIter[ord(s2[right])] -= 1
                        right += 1
                    else:
                        break
                left += 1
                right = left + 1


                if sum(strArrIter) == 0 :
                    return True

            else:
                left += 1
                right = left + 1

            

            if sum(strArrIter) == 0 :
                return True
        
        return False

        
        