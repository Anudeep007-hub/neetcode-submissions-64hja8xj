class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        R,C = len(grid), len(grid[0])
        vis = [[False]*C for _ in range(R)]

        def dfs(i,j,R,C):
            vis[i][j] = True

            dist = [(-1,0), (1,0), (0,1), (0,-1)]
            for a,b in dist:
                if 0<=a+i<R and 0<=b+j<C:
                    if grid[a+i][b+j] == '1' and not vis[a+i][b+j]:
                        dfs(a+i,b+j,R,C) 
        
        count = 0 

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1' and not vis[i][j]:
                    count += 1
                    dfs(i,j,R,C) 
        return count
        