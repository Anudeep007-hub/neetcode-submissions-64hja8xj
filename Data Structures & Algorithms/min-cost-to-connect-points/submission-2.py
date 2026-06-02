class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 

        vis = set() 
        n = len(points) 
        adj = {i:[] for i in range(n)} # (cost, node)
        minH = [(0,0)] # (cost, node) 
        tCost = 0  

        for i in range(n):
            x1,y1 = points[i] 
            for j in range(i+1,n):
                x2,y2 = points[j] 
                dist = abs(x1-x2) + abs(y1-y2) 
                adj[i].append((dist, j)) 
                adj[j].append((dist, i)) 

        # Prims 

        while len(vis) < n:
            nodeCost, node = heapq.heappop(minH) 
            if node in vis:
                continue 
            tCost += nodeCost 
            vis.add(node) 

            for neiCost, neiNode in adj[node]:
                heapq.heappush(minH, (neiCost, neiNode)) 

        return tCost

        