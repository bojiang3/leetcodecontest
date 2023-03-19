class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        s = str(bin(n))
        s = s.split("b")[1]
        print(s)
        even = odd = 0
        s = s[::-1]
        for i in range(len(s)):
            if i % 2 == 0 and s[i] == "1":
                even += 1
            elif i % 2 == 1 and s[i] == "1":
                odd += 1
        
        return [even, odd]
        
        