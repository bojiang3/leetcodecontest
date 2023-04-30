class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        coordinates = {}
        
        m, n = len(mat), len(mat[0])
        cols = [n] * m
        rows = [m] * n
        for i in range(m):
            for j in range(n):
                coordinates[mat[i][j]] = (i, j)
        
        for i in range(len(arr)):            
            x, y = coordinates[arr[i]]
            cols[x] -= 1
            if cols[x] == 0:
                return i
            rows[y] -= 1
            if rows[y] == 0:
                return i
        return m * n - 1
            