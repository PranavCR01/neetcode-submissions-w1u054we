class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(-1,0), (1, 0), (0,1), (0,-1)]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return 
            board[r][c] = 'S'
            for dr, dc in directions:
                nr, nc =  r + dr, c + dc
                dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                    dfs(r, c)
     
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                

                

                
            

        