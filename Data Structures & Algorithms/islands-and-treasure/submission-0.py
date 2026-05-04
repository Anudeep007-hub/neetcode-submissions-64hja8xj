from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        R, C = len(grid), len(grid[0]) 
        INF = 2**31-1

        def bfs(que,R,C):
            nonlocal INF

            while que:
                r,c,d = que.popleft()  
                dist = [(-1,0), (1,0), (0,1), (0,-1)] 
                for i, j in dist:
                    nr,nc = r+i, c+j 
                    if 0<= nr<R and 0<= nc<C and grid[nr][nc] == INF: 
                        grid[nr][nc] = d+1 
                        que.append((nr,nc,d+1))  
            return
             




        # Call the traversal function 
        que = deque() 
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: 
                    que.append((r,c,0)) 

        bfs(que,R,C)
        