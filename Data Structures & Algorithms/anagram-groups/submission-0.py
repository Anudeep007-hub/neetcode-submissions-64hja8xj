from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  

        hash_map = {}

        for string in strs: 
            tmp = tuple(sorted(string, key=str.lower))
            if tmp in hash_map:
                hash_map[tmp] += [string]
            else:
                hash_map[tmp] = [string] 

        ans = []

        for i in hash_map.values():
            ans.append(i)
        


        return ans



        