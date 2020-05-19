import math


class Sudoku:
    x = 9
    y = 9
    init_board = [[0] * 9 for i in range(9)]

    def __init__(self, board):
        with open(board, "r") as sudoku_board:
            row = 0
            for line in sudoku_board:
                if row > 8:
                    raise IndexError("Too many rows in file")
                line = line.strip()
                sudoku_line = line.split(" ")
                if len(sudoku_line) > 9:
                    raise IndexError("Too many values in column")
                for pos in range(len(sudoku_line)):
                    if sudoku_line[pos] != 0:
                        self.init_board[row][pos] = sudoku_line[pos]
                row = row + 1

    def printboard(self):
        for row in self.init_board:
            print(" ".join(row))

    def check_columns(self, row, column, value):
        for y in range(len(self.init_board)):
            if self.init_board[y][int(column)-1] == value:
                return False
        return True

    def check_row(self, row, column, value):
        insert_row = self.init_board[int(row)-1]
        if value in insert_row:
            return False
        else:
            return True

    def check_quadrant(self, row, column, value):
        lower_row_quadrant, upper_row_quadrant, lower_column_quadrant, upper_column_quadrant = self.set_quadrant_limits(row, column)

        for y in range(lower_row_quadrant, upper_row_quadrant+1):
            for x in range(lower_column_quadrant, upper_column_quadrant):
                if self.init_board[y][x] == value:
                    return False
        return True

    def print_quadrant(self, row, column):
        lower_row_quadrant, upper_row_quadrant, lower_column_quadrant, upper_column_quadrant = self.set_quadrant_limits(row, column)
        for y in range(lower_row_quadrant, upper_row_quadrant+1):
            quadrant_row = self.init_board[y]

            print(" ".join(quadrant_row[lower_column_quadrant:upper_column_quadrant+1]))

    def set_quadrant_limits(self, row, column):
        lower_row_quadrant = math.floor((int(row)-1)/3)*3
        upper_row_quadrant = math.floor((int(row)-1)/3)*3+2

        lower_column_quadrant = math.floor((int(column)-1)/3)*3
        upper_column_quadrant = math.floor((int(column)-1)/3)*3+2

        return lower_row_quadrant, upper_row_quadrant, lower_column_quadrant, upper_column_quadrant

    def play(self):
        self.printboard()
        while True:
            row = input("Row number (1-9) ")
            if int(row) < 1 or int(row) > 9:
                print("Invalid value. Must be between 1 and 9")
                continue

            column = input("Column number (1-9) ")
            if int(column) < 1 or int(column) > 9:
                print("Invalid value. Must be between 1 and 9")
                continue

            value = input("Value to be inserted ")
            if int(value) < 1 or int(value) > 9:
                print("Invalid value. Must be between 1 and 9")
                continue

            if not self.check_columns(row, column, value):
                print("Value already exists in column", column, ", try again")
            elif not self.check_row(row, column, value):
                print("Value already exists in row", row, ", try again")
            elif not self.check_quadrant(row, column, value):
                self.print_quadrant(row, column)
                print("Value already exists in quadrant")
            else:
                self.init_board[int(row)-1][int(column)-1] = value
                print("BOARD UPDATED")
                self.printboard()


game = Sudoku("/home/k27549/Documents/Projects/Personal/testboard.txt")
game.play()