class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checking individual grids
        grid1 = board[0][0:3] + board[1][0:3] + board[2][0:3] 
        grid4 = board[3][0:3] + board[4][0:3] + board[5][0:3] 
        grid7 = board[6][0:3] + board[7][0:3] + board[8][0:3] 

        grid2 = board[0][3:6] + board[1][3:6] + board[2][3:6] 
        grid5 = board[3][3:6] + board[4][3:6] + board[5][3:6] 
        grid8 = board[6][3:6] + board[7][3:6] + board[8][3:6] 

        grid3 = board[0][6:9] + board[1][6:9] + board[2][6:9] 
        grid6 = board[3][6:9] + board[4][6:9] + board[5][6:9] 
        grid9 = board[6][6:9] + board[7][6:9] + board[8][6:9] 
        
        grids = [grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9]
        for grid in grids:
            appeared = []
            for e in grid:
                if e in appeared:
                    return False
                elif e != '.':
                    appeared.append(e)

        #checking columns 
        for i in range(0, 9):
            appeared = []
            for row in board:
                if row[i] in appeared:
                    return False
                elif row[i] != ".":
                    appeared.append(row[i])
        
        #checking rows
        for row in board:
            appeared = []
            for e in row:
                if e in appeared:
                    return False
                elif e != '.':
                    appeared.append(e)
        
        return True