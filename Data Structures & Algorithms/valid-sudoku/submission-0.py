class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    box_index = (i//3)*3 + (j//3)

                    if (num in rows[i]) or (num in column[j]) or (num in square[box_index]):
                        return False

                    rows[i].add(num)
                    column[j].add(num)
                    square[box_index].add(num)

        return True
