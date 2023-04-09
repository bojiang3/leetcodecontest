class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        l = len(nums)
        total = {}
        res = []
        for i, n in enumerate(nums):
            if n in total:
                total[n].append(i)
            else:
                total[n] = [i]
        
        res_dict = {}
        visited = set()
        for i, n in enumerate(nums):
            if n in visited:
                continue
            indices = total[n]
            visited.add(n)
            tmp = sum([abs(indices[0] - index) for index in indices])
            res_dict[n] = deque([tmp])
            print(tmp)
            summ = tmp
            for i in range(1, len(indices)):
                tmp = tmp + (i - 1) * abs((indices[i] - indices[i - 1])) - (len(indices) - i - 1) * abs((indices[i] - indices[i - 1]))
                
                res_dict[n].append(tmp)
                
            
        
        for i, n in enumerate(nums):
            now = res_dict[n].popleft()
            res.append(now)
        
        return res
    
