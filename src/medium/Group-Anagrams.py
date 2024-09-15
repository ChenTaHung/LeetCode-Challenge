"""
49. Group Anagrams

Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # ans = []
        # recognized = []

        # for s in strs:
        #     sort_s = sorted(s)
        #     if sort_s not in recognized:
        #         recognized += [sort_s]
        #         ans += [[s]]

        #     else:
        #         sel_id = recognized.index(sort_s)
        #         ans[sel_id].append(s)
        
        # return ans

        defdict = defaultdict(list)

        for s in strs:
            sortstr = ''.join(sorted(s))
            defdict[sortstr].append(s)

        return list(defdict.values())