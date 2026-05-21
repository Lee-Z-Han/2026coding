# week13-2.py 學習計畫 Graph - BFS 第2題
# LeetCode 994. Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M,N = len(grid), len(grid[0]) # 長, 寬
        visited = set()
        queue = deque()
        # queue.append( (i,j,0) ) # 把爛掉的橘子, 放入 queue
        fresh = 0 # 先統計有幾個新鮮的橘子
        for i in range(M):
            for j in range(N):
                if grid[i][j]==2: 
                    visited.add( (i,j) )
                    queue.append( (i,j,0) )
                if grid[i][j]==1: fresh += 1 # 多1個新鮮的橘子
        if fresh==0: return 0 # 題目如果都沒新鮮的橘子, 竟然要 return 0
        ans = -1 # 甚麼時候全部爛掉? 不知道。一開始 -1 沒有爛掉
        while queue:
            i,j,t = queue.popleft()
            ans = t # 更新爛掉的時間!
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if ii<0 or jj<0 or ii>=M or jj>=N: continue
                if (ii,jj) in visited: continue
                if grid[ii][jj]==1:  # 這格是還沒爛掉的橘子, 可感染它!
                    fresh -= 1 # 好可憐, 它爛掉了
                    visited.add( (ii,jj) )
                    queue.append( (ii,jj,t+1) ) # 將在 t+1 時爛掉
        if fresh>0: return -1 # 只要還有任何一顆還沒爛掉、還是新鮮的, 就沒有輸
        return ans