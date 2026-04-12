class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Return true if the Sudoku board is valid, otherwise return false
        # Note: A board does not need to be full or be solvable to be valid.

        # Each row must contain the digits 1-9 without duplicates.
        # Each column must contain the digits 1-9 without duplicates.
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
        digits = [str(i) for i in range(1, 10)]
        for i in range(9):
            row_check, col_check, box_check = [], [], []
            for j in range(9):
                # check rows
                if board[i][j] in digits:
                    if board[i][j] in row_check:
                        return False
                    row_check.append(board[i][j])
                # check columns
                if board[j][i] in digits:
                    if board[j][i] in col_check:
                        return False
                    col_check.append(board[j][i])
                # check boxes
                box_row = (i//3)*3 + (j//3)
                box_col = (i %3)*3 + (j %3)
                if board[box_row][box_col] in digits:
                    if board[box_row][box_col] in box_check:
                        return False
                    box_check.append(board[box_row][box_col])

        return True