# Left as-is. Not finished during contest

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        counts = defaultdict(int)
        E = defaultdict(list)
        for u, v in edges:
            E[u].append(v)
            E[v].append(u)
        
        for start, end in trips:
            q = deque()
            q.append((start, [start]))
            print(q)
            visited = set()
            while q:
                
                cur, [path] = q.popleft()
                
                if cur in visited:
                    continue
                visited.add(cur)
                path.append(cur)
                
                if cur == end:
                    for node in path:
                        counts[node] += 1
                    break
                q.extend(E[cur])
        
        print(counts)
                    
            