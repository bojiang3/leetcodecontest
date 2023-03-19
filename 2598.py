import collections
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        nums = sorted(nums)
        
        remainders = [num % value for num in nums]
        count = collections.Counter(remainders)
        
        sett = set(remainders)
        for i in range(len(nums)):
            tmp = i % value
            if tmp in count:
                count[tmp] -= 1
                if count[tmp] == 0:
                    del count[tmp]
            else:
                return i
        
        
        return len(nums)
        