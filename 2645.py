class Solution:
    def addMinimum(self, word: str) -> int:
        # cbca
        # babcac
        # 012345
        last = 0
        res = 0
        for char in word:
            if char == "a":
                if last == 0:
                    last += 1
                elif last == 1:
                    res += 2
                    last = 1
                else:
                    res += 1
                    last = 1
            elif char == "b":
                if last == 1:
                    last += 1
                elif last == 0:
                    res += 1
                    last = 2
                else:
                    res += 2
                    last = 2
            else:
                if last == 2:
                    last = 0
                    continue
                elif last == 1:
                    res += 1
                    last = 0
                else:
                    res += 2
        
        if last == 2:
            res += 1
        elif last == 1:
            res += 2
        
        return res
                        