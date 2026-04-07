class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        vis = [False]*n
        adj = [[] for _ in range(n)]
        comp = 0 
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        


        def dfs(node,vis,adj):
            vis[node] = True 
            for adjNode in adj[node]:
                if not vis[adjNode]:
                    dfs(adjNode,vis,adj) 
            return



        for node in range(n):
            if not vis[node]:
                dfs(node,vis,adj)
                comp+= 1 
        return comp
        