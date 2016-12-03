from locale import atoi

__author__ = 'Bio'

from graphics import *


def initialize_board(filename):
    infile = open(filename, "r")
    line = infile.readline()
    infile.close()
    data = str(line).split()
    board = []
    for i in range(6):
        board.append([])
    i = 0
    for row in range(6):
        for col in range(6):
            column_value = atoi(data[i])
            board[row].append(column_value)
            i += 1
    return board


def display_numbers(window, board):
    for row in range(6):
        for col in range(6):
            square = Rectangle(Point(col * 50, row * 50), Point((col + 1) * 50, (row + 1) * 50))
            square.setFill("white")
            square.draw(window)
            if board[row][col] != 0:
                center = Point(col * 50 + 25, row * 50 + 25)
                number = Text(center, board[row][col])
                number.setSize(26)
                number.setTextColor("purple")
                number.draw(window)


def update_board(board, row, col):
    if row > 0 and board[row - 1][col] == 0:
        board[row - 1][col] = board[row][col]
        board[row][col] = 0
        return
    if row < 5 and board[row + 1][col] == 0:
        board[row + 1][col] = board[row][col]
        board[row][col] = 0
        return
    if col > 0 and board[row][col - 1] == 0:
        board[row][col - 1] = board[row][col]
        board[row][col] = 0
        return
    if col < 5 and board[row][col + 1] == 0:
        board[row][col + 1] = board[row][col]
        board[row][col] = 0
        return


def check_for_winner(board):
    num = 1
    row = 0
    col = 0
    while num <= 35:
        if board[row][col] == num:
            num = num + 1
            col = col + 1
            if col > 5:
                col = 0
                row = row + 1
        else:
            return False
    return True


def main():
    filename = input("Input name of puzzle file: ")
    window = GraphWin("Puzzle 35", 300, 300)
    board = initialize_board(filename)
    display_numbers(window, board)
    game_over = False
    while not game_over:
        p = window.getMouse()
        col = int(p.getX() / 50)  # compute column where player clicked
        row = int(p.getY() / 50)  # compute row where player clicked
        update_board(board, row, col)
        display_numbers(window, board)
        game_over = check_for_winner(board)
    message = Text(Point(150, 150), "GG")
    message.setSize(35)
    message.setTextColor("orange")
    message.draw(window)
    window.getMouse()
    window.close()


main()