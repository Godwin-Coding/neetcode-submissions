class Solution:
    def isValidSudoku(self, board):
        hash_grid = dict()
        hash_row = dict()
        hash_col = dict()

        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] == ".":
                    continue
                
                #check grid
                grid_id = (r//3, c//3)
                if grid_id not in hash_grid:
                    hash_grid[grid_id] = set()
                if board[r][c] in hash_grid[grid_id]:
                    return False
                else:
                    hash_grid[grid_id].add(board[r][c])

                #check row
                if r not in hash_row:
                    hash_row[r] = set()
                if board[r][c] in hash_row[r]:
                    return False
                else:
                    hash_row[r].add(board[r][c])

                #check col
                if c not in hash_col:
                    hash_col[c] = set()
                if board[r][c] in hash_col[c]:
                    return False
                else:
                    hash_col[c].add(board[r][c])
                
        return True

