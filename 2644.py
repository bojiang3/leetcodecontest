class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        
        scores = []
        for i in range(len(divisors)):
            d = divisors[i]
            score = 0
            for n in nums:
                if n % d == 0:
                    score += 1
            scores.append((score, i))
        
        
        scores.sort(reverse=True)
        
        maxx = scores[0][0]
        toReturn = set()
        for pair in scores:
            if pair[0] == maxx:
                i = pair[1]
                toReturn.add(divisors[i])
            else:
                break
        
        return min(toReturn)
        
        
            
        