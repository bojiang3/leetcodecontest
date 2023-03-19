class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid[0])
        x, y = 0, 0
        cur = 0
        directions = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for i in range(n ** 2):
            flag = False
            
            for dx, dy in directions:
                tx, ty = x + dx, y + dy
                if 0 <= tx < n and 0 <= ty < n:
                    if grid[tx][ty] == cur + 1:
                        flag = True
                        x, y = tx, ty
                        
                        break
            if cur == n ** 2 - 1:
                return True
            if flag:
                cur += 1
            else:
                print(cur, x, y)
                return False
        
        return True
            
                
        