from collections import deque, defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int: 

        dist = [float('inf')]*(n+1)  
        dist[k] = 0
        que = deque([(0,k)])  # (cost, node) 
        adj = defaultdict(list) # (cost, node)

        for u,v,t in times:
            adj[u].append((t,v))

        while que: 
            cost, node = que.popleft() 
            for neiCost, neiNode in adj[node]:
                totCost = cost+neiCost 
                if totCost < dist[neiNode]:
                    dist[neiNode] = totCost 
                    que.append((totCost, neiNode))  

        minTime = -1

        for i in range(1,n+1):
            if dist[i] == float('inf'):
                return -1  
            minTime = max(minTime, dist[i])

        return minTime

                

        