class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = [[]]
        for num in nums:
            tmp = [item + [num] for item in res if num + k not in set(item) and num - k not in set(item)]
            res += tmp
        
        
        return len(res) - 1
            