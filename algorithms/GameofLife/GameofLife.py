class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        if n == 0 or m == 0:
            return
        
        def livecounter(board, i, j):
            c = 0
            for I in range(max(i-1, 0), min(i+2, n)):
                for J in range(max(j-1, 0), min(j+2, m)):
                    c += board[I][J] & 1
            return c
        
        for i in range(n):
            for j in range(m):
                count = livecounter(board, i, j)
                if count == 3 or count - board[i][j] == 3:
                    board[i][j] |= 2
        
        for i in range(n):
            for j in range(m):
                board[i][j] >>= 1
