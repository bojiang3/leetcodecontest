class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        n = len(nums)
        if n == 0 or n == 1:
            return 0
        diffs = [abs(nums[i] - nums[i - 1]) for i in range(1, n)]
        
        def check(mx):
            dp0 = dp1 = 0
            for x in diffs:
                if x > mx:
                    dp0 = dp1
                else:
                    dp0, dp1 = dp1, max(dp1, dp0 + 1)
            return dp1
        
        return bisect_left(range(max(diffs)), p, key=check)
        