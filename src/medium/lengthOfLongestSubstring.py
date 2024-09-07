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