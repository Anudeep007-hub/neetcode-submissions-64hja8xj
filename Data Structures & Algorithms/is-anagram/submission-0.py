class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        s_hash = {} 
        t_hash = {} 
 
        for let in s:
            s_hash[let] = s_hash.get(let,0)+1
        for let in t:
            t_hash[let] = t_hash.get(let,0)+1 

        return s_hash == t_hash 
        