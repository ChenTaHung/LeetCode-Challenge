"""
659. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        if not strs:
            return ""
        
        ans = []
        
        for s in strs:
            code = []
            for ss in s:
                code.append(str(ord(ss)))
                
            ans.append(code)

        return ans
        

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, strs):
        if not str:
            return []
        
        ans = []
        for s in strs :
            string = []
            for ss in s:
                string.append(chr(int(ss)))
                
            ans.append(''.join(string))
        
        return ans