class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.E = defaultdict(list)
        for u, v, w in edges:
            self.E[u].append((v, w))
        self.n = n
        
        
    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.E[u].append((v, w))
        
        
    def shortestPath(self, node1: int, node2: int) -> int:
        q = [(0, node1)]
        heapq.heapify(q)
        visited = set()
        
        while q:
            cost, cur = heapq.heappop(q)
            if cur in visited:
                continue
            visited.add(cur)
            
            if cur == node2:
                return cost
            
            for v, w in self.E[cur]:
                
                heapq.heappush(q, (cost + w, v))
                
                
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)