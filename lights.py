__author__ = 'Bio'

from graphics import *

def initialize_board(filename):
    infile = open(filename, "r")
    board = []
    for i in range(5):
        board.append([])
    for row in range(5):
        for col in range(5):
            columnvalue = eval(infile.readline())
            board[row].append(columnvalue)
    return board

def draw_lines(window):
    line1 = Line(Point(0,50),Point(250,50))
    line1.draw(window)
    line2 = Line(Point(0,100),Point(250,100))
    line2.draw(window)
    line3 = Line(Point(0,150),Point(250,150))
    line3.draw(window)
    line4 = Line(Point(0,200),Point(250,200))
    line4.draw(window)
    line5 = Line(Point(50,0),Point(50,250))
    line5.draw(window)
    line6 = Line(Point(100,0),Point(100,250))
    line6.draw(window)
    line7 = Line(Point(150,0),Point(150,250))
    line7.draw(window)
    line8 = Line(Point(200,0),Point(200,250))
    line8.draw(window)

def display_lights(window, board):
    for row in range(5):
        for column in range(5):
            center = Point(column*50+25,row*50+25)
            circ = Circle(center,25)
            if (board[row][column] == 1):
                circ.setFill("yellow")
            else:
                circ.setFill("white")
            circ.draw(window)

def update_board(board, row, column):
    # toggle chosen light in the given row and column
    if board[row][column] == 1:
        board[row][column] = 0
    else:
        board[row][column] = 1
    if row > 0: # is there a light above the chosen light?
        if board[row-1][column] == 1:
            board[row-1][column] = 0
        else:
            board[row-1][column] = 1
    if row < 4: # is there a light below the chosen light?
        if board[row+1][column] == 1:
            board[row+1][column] = 0
        else:
            board[row+1][column] = 1
    if column > 0: # is there a light to the left of the chosen light?
        if board[row][column-1] == 1:
            board[row][column-1] = 0
        else:
            board[row][column-1] = 1
    if column < 4: # is there a light to the right of the chosen light?
        if board[row][column+1] == 1:
            board[row][column+1] = 0
        else:
            board[row][column+1] = 1

def check_for_winner(board):
    sum = 0
    for row in range(5):
        for column in range(5):
            if board[row][column]:
                return False
    return True

def main():
    filename = input("Input name of puzzle file: ")
    window = GraphWin("Lights Out", 250, 250)
    board = initialize_board(filename)
    draw_lines(window)
    display_lights(window,board)
    game_over = False
    while game_over == False:
        p = window.getMouse()
        print(p.getX()," ",p.getY()) # see where player clicked
        column = int(p.getX()//50) # compute column where player clicked
        row = int(p.getY()//50) # compute row where player clicked
        update_board(board, row, column)
        display_lights(window,board)
        game_over = check_for_winner(board)

    print("GAME OVER")
    window.getMouse()
    window.close()
main()