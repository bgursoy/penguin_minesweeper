from PyQt5 import QtGui
from PyQt5.QtWidgets import QPushButton, QSizePolicy


class Button(QPushButton):

    def __init__(self, row, column, parent):
        super().__init__()
        self.row = row
        self.column = column
        self.parent_window = parent

        self.setText(" ")
        self.setStyleSheet("background-color: #4e4f59")
        self.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.parent_window.actionButtonClick(self)
