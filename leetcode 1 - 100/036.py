class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # row
            if not all(v == 1 for k, v in Counter(board[i]).items() if k != '.'):
                return False

            # column
            if not all(v == 1 for k, v in Counter([board[j][i] for j in range(9)]).items() if k != '.'):
                return False

            # matrix            
            if not all(v == 1 for k, v in Counter([board[(i%3)*3 + j%3][(i//3)*3 + j//3] for j in range(9)]).items() if k != '.'):
                return False

        return True
