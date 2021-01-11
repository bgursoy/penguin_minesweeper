from random import randint as random


class Matrix:

    def __init__(self, row, col, mine):
        self.matrix = []
        self.row = row
        self.col = col
        self.mine = mine

        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append(0)
            self.matrix.append(row)

        mine = 0
        while mine != self.mine:
            m = random(0, self.row - 1)
            n = random(0, self.col - 1)
            if self.matrix[m][n] != "X":
                self.matrix[m][n] = "X"
                mine += 1

        for i in range(self.row):
            for j in range(self.col):
                if self.matrix[i][j] == "X":
                    if i < self.row - 1 and self.matrix[i + 1][j] != "X":
                        self.matrix[i + 1][j] += 1
                    if i > 0 and self.matrix[i - 1][j] != "X":
                        self.matrix[i - 1][j] += 1
                    if j < self.col - 1 and self.matrix[i][j + 1] != "X":
                        self.matrix[i][j + 1] += 1
                    if j > 0 and self.matrix[i][j - 1] != "X":
                        self.matrix[i][j - 1] += 1
                    if i < self.row - 1 and j < self.col - 1 and self.matrix[i + 1][j + 1] != "X":
                        self.matrix[i + 1][j + 1] += 1
                    if i > 0 and j > 0 and self.matrix[i - 1][j - 1] != "X":
                        self.matrix[i - 1][j - 1] += 1
                    if i < self.row - 1 and j > 0 and self.matrix[i + 1][j - 1] != "X":
                        self.matrix[i + 1][j - 1] += 1
                    if i > 0 and j < self.col - 1 and self.matrix[i - 1][j + 1] != "X":
                        self.matrix[i - 1][j + 1] += 1
                else:
                    continue
