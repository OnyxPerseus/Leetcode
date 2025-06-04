def solve(board):
    return validRows(board) and validCols(board) and validAreas(board)


def validRows(board):
    for i in range(9):
        remember = [False] * 10
        for j in range(9):
            if board[i][j].isdigit():
                value = int(board[i][j])
                if remember[value]:
                    return False
                remember[value] = True
    return True


def validCols(board):
    for i in range(9):
        remember = [False] * 10
        for j in range(9):
            if board[j][i].isdigit():
                value = int(board[j][i])
                if remember[value]:
                    return False
                remember[value] = True
    return True


def validAreas(board):
    for k in range(9):
        remember = [False] * 10
        for i in range(3):
            for j in range(3):
                r = k // 3 * 3 + i
                c = k % 3 * 3 + j
                if board[r][c].isdigit():
                    value = int(board[r][c])
                    if remember[value]:
                        return False
                    remember[value] = True
    return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    print(solve(board))
