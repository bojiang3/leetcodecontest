# Didn't finish. Left as-is

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        tmp = grid[0][0]
        if grid[0 + tmp][0] == 0 and grid[0][0 + tmp] == 0 or grid[0][0] == 0:
            return -1
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = 1
        dp[0][1] = dp[1][0] = dp[1][1] = 2
        
        q = deque([(0, 0)])
        
        while q:
            x, y = q.popleft()
            dx = dy = dp[x][y]
            for i in range(1, min(dx + 1, m)):
                print("i=", i, "y=", y)
                dp[i][y] = dp[x][y] + 1
                if i == m - 1 and y == n - 1:
                    return dp[m - 1][n - 1]
                q.append((i, y))
            for j in range(1, min(dy + 1, n)):
                dp[x][j] = dp[x][y] + 1
                if x == m - 1 and j == n - 1:
                    return dp[m - 1][n - 1]
                q.append((x, j))
        
        return -1
            
        