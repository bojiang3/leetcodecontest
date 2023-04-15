class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        conver = [0] * n
        maxes = [0] * n
        maxes[0] = nums[0]
        prefix = 0
        res = [0] * n
        res[0] = 2 * nums[0]
        
        for i in range(1, n):
            maxes[i] = max(maxes[i - 1], nums[i])
            conver[i] = maxes[i] + nums[i]
            res[i] = res[i - 1] + conver[i]
            
        return res