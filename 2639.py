class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        col = 0
        for row in grid:
            if len(row) > col:
                col = len(row)
        
        res = [0] * col
        
        for row in grid:
            for i in range(len(row)):
                cur = row[i]
                if cur >= 0:
                    l = len(str(cur))
                else:
                    l = len(str(abs(cur))) + 1
                    
                res[i] = max(res[i], l)
        
        return res
        