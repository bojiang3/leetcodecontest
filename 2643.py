class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxx = 0
        index = -1
        for i in range(len(mat) - 1, -1, -1):
            row = mat[i]
            count = sum(row)
            if count >= maxx:
                maxx = count
                index = i
        
        return [index, maxx]