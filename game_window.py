import time

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QSizePolicy
from game_layout import Ui_GameWindow
from button import Button
from matrix import Matrix


class GameWindow:
    setup_ui = Ui_GameWindow()

    def __init__(self, y, x, mine, min_width, min_height, max_width, max_height, size_width, size_height, main_window, level):
        self.count = 0
        self.game_map = []
        self.y = y
        self.x = x
        self.mine = mine
        self.mainWindow = main_window
        self.level = level

        self.field = Matrix(y, x, mine)

        self.win = QMainWindow()
        self.setup_ui.setupUi(self.win, min_width, min_height, max_width, max_height, size_width, size_height)
        self.win.setWindowTitle("Penguin Minesweeper")
        self.win.setWindowIcon(QIcon("penguin_mine_icon.png"))

        # Connect
        self.setup_ui.newGameButton.clicked.connect(self.newGame)
        self.setup_ui.difficultyButton.clicked.connect(self.changeDifficulty)

        # Fill grid layout with buttons
        for row in range(y):
            button_row = []
            for col in range(x):
                game_button = Button(row, col, self)
                button_row.append(game_button)
                self.setup_ui.gridLayout.addWidget(game_button, row, col)
            self.game_map.append(button_row)

    def revealAnswer(self, row, col):
        button = self.game_map[row][col]

        if not button.isEnabled():
            return

        self.count += 1
        button.setText(str(self.field.matrix[row][col]))
        button.setStyleSheet("background-color: #e9e3f4; color: black; font-weight: bold; font-size: 20px")
        button.setEnabled(False)

        if self.count == (self.y * self.x) - self.mine:
            end = QMessageBox.question(self.win, "Game Over", "Do you want to play again?", QMessageBox.Yes, QMessageBox.No)
            if end == QMessageBox.No:
                self.win.close()
            if end == QMessageBox.Yes:
                self.newGame()

        if self.field.matrix[row][col] == 0:
            button.setStyleSheet("background-color: #c5d5ea")

        if self.field.matrix[row][col] == 0:
            button.setText(" ")
            if row < self.y - 1:
                self.revealAnswer(row + 1, col)
            if row > 0:
                self.revealAnswer(row - 1, col)
            if col < self.x - 1:
                self.revealAnswer(row, col + 1)
            if col > 0:
                self.revealAnswer(row, col - 1)
            if row < self.y - 1 and col < self.x - 1:
                self.revealAnswer(row + 1, col + 1)
            if row > 0 and col > 0:
                self.revealAnswer(row - 1, col - 1)
            if row < self.y - 1 and col > 0:
                self.revealAnswer(row + 1, col - 1)
            if row > 0 and col < self.x - 1:
                self.revealAnswer(row - 1, col + 1)

        if self.field.matrix[row][col] == "X":
            self.makeIcon(row, col)

    def actionButtonClick(self, target):
        row = target.row
        col = target.column
        self.revealAnswer(row, col)

    def show(self):
        self.win.show()

    def newGame(self):
        self.field = Matrix(self.y, self.x, self.mine)
        self.count = 0
        for i in range(self.y):
            for j in range(self.x):
                button = self.game_map[i][j]
                button.setText(" ")
                button.setStyleSheet("background-color: #4e4f59")
                button.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
                button.setIcon(QIcon(""))
                button.setEnabled(True)

    def changeDifficulty(self):
        self.mainWindow.show()
        self.win.close()

    def makeIcon(self, row, col):
        self.button = self.game_map[row][col]
        self.button.setText(" ")
        self.size = self.setSize()
        self.pixmap_red = QPixmap("penguin_red_icon.png")
        self.pixmap_blue = QPixmap("penguin_blue_icon.png")
        self.icon_red = QIcon()
        self.icon_red.addPixmap(self.pixmap_red, QIcon.Disabled, QIcon.Off)
        self.icon_blue = QIcon()
        self.icon_blue.addPixmap(self.pixmap_blue, QIcon.Disabled, QIcon.On)
        for i in range(self.y):
            for j in range(self.x):
                buttons = self.game_map[i][j]
                if self.field.matrix[i][j] == "X":
                    buttons.setText(" ")
                    buttons.setIcon(self.icon_blue)
                    buttons.setIconSize(self.size)
                buttons.setEnabled(False)
        self.button.setIcon(self.icon_red)

    def setSize(self):
        if self.level == "easy":
            self.size = QSize(30, 30)
        if self.level == "mid":
            self.size = QSize(24, 24)
        if self.level == "hard":
            self.size = QSize(22, 22)
        if self.level == "custom":
            width_size = 38 - self.y
            height_size = 38 - self.x
            self.size = QSize(width_size, height_size)
        return self.size
