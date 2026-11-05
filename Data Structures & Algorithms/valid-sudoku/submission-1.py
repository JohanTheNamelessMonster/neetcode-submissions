class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            vals_seen  = {str(k) : 0 for k in range(1,10)}
            for j in range(9):
                if board[j][i] != ".":
                    vals_seen[board[j][i]] += 1
                    if vals_seen[board[j][i]]  > 1:
                        return False
        
        for i in range(9):
            vals_seen  = {str(k) : 0 for k in range(1,10)}
            for j in range(9):
                if board[i][j] != ".":
                    vals_seen[board[i][j]] += 1
                    if vals_seen[board[i][j]]  > 1:
                        return False

        for s in range(9):
            row = s // 3
            col = s % 3
            vals_seen  = {str(k) : 0 for k in range(1,10)}
            for k in range(3):
                for l in range(3):
                    if board[3*row + k][3*col + l] != ".":
                        vals_seen[board[3*row + k][3*col + l]] += 1
                        if vals_seen[board[3*row + k][3*col + l]] > 1:
                            return False
        return True