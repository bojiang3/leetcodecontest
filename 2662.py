# Sollution not working. Left as-is

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        new_special = []
        roads = {}
        valid = 0
        for r in specialRoads:
            x1, y1, x2, y2, cost = r
            if cost > abs(x2 - x1) + abs(y2 - y1):
                continue
            valid += 1
            roads[(r[0], r[1])] = (r[2], r[3], r[4])
        
        
        if valid == 0:
            
            return target[1] - start[1] + (target[0] - start[0])
        
            
        
        stack = deque([(start[0], start[1], 0)])
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = []
        while stack:
            curx, cury, cost = stack.popleft()
            if [curx, cury] == target:
                res.append(cost)
                continue
            if (curx, cury) in visited:
                continue
            visited.add((curx, cury))
            for dx, dy in directions:
                tx, ty = curx + dx, cury + dy
                if tx > target[0] or tx < start[0] or ty > target[1] or ty < start[1]:
                    continue
                if (tx, ty) in roads:
                    visited.add((tx, ty))
                    nx, ny, tmp_cost = roads[(tx, ty)]
                    
                    stack.append((nx, ny, cost + tmp_cost + 1))
                
                stack.append((tx, ty, cost + 1))
        
        print(res)
        return min(res)
                    
        
        
        
        