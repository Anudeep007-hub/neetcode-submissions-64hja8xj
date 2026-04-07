from collections import Counter 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        que = []
        hash_map = Counter(nums)

        for num,freq in hash_map.items():
            heapq.heappush(que, (freq,num)) 

            if len(que)>k:
                heapq.heappop(que) 

        return [num for freq,num in que]
        
        

        