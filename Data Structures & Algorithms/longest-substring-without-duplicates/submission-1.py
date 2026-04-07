class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 

        i,j = 0,0 
        n = len(s)
        longest = 0
        hash_set = set()

        while j<n:
            if s[j] not in hash_set: 
                hash_set.add(s[j])
                j += 1 
                longest = max(longest, j-i) 
            else:
                hash_set.remove(s[i]) 
                i+= 1 
        
        return longest

        