class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        last = -10
        p1, p2 = 0, 0
        for i in range(n):
            if i - last > 2:
                if player1[i] == 10:
                    last = i
                p1 += player1[i]
            else:
                if player1[i] == 10:
                    last = i
                p1 += 2 * player1[i]
        
        last = -10
        for i in range(n):
            if i - last > 2:
                if player2[i] == 10:
                    last = i
                p2 += player2[i]
            else:
                if player2[i] == 10:
                    last = i
                p2 += 2 * player2[i]
        
        if p1 == p2:
            return 0
        return 1 if p1 > p2 else 2
        
            
                
                