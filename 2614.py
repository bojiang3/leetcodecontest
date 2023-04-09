# 2614. Prime In Diagonal

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        diagonal = []
        m, n = len(nums), len(nums[0])
        for i in range(m):
            for j in range(n):
                if i == j or i == n - j - 1:
                    diagonal.append(nums[i][j])
        
        diagonal = sorted([n for n in set(diagonal)], reverse=True)
        upper = diagonal[0]
        is_prime = [True] * (upper + 1)
        
        
#         end = int(math.sqrt(upper))
#         for i in range(2, upper // 2):
#             for j in range(i + 1, upper // 2):
#                 if  i * j < upper:
#                     is_prime[i * j] = False
        
        def is_p(num):
            if num < 2: return False
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    return False
            return True
        for num in diagonal:
            if is_p(num):
                return num
        
        
        return 0
        
        
        