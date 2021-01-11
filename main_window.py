from PyQt5.QtWidgets import QMainWindow
from custom_layout import Ui_CustomWindow
from game_window import GameWindow
from main_layout import Ui_MainWindow


class MainWindow:
    setup_ui = Ui_MainWindow()
    custom_ui = Ui_CustomWindow()

    def __init__(self):
        self.win = QMainWindow()
        self.setup_ui.setupUi(self.win)
        self.win.setWindowTitle("Penguin Minesweeper")
        self.setup_ui.easyLevelButton.clicked.connect(self.actionELB)
        self.setup_ui.midLevelButton.clicked.connect(self.actionMLB)
        self.setup_ui.hardLevelButton.clicked.connect(self.actionHLB)
        self.setup_ui.customButton.clicked.connect(self.actionCB)

        self.custom_win = QMainWindow()
        self.custom_ui.setupUi(self.custom_win)
        self.custom_win.setWindowTitle("Custom")

    def show(self):
        self.win.show()

    def actionELB(self):
        self.level = "easy"
        # Create a new game window
        self.game_window = GameWindow(8, 8, 10, 500, 500, 800, 600, 800, 700, self, self.level)
        self.game_window.show()

        # Close this window
        self.win.close()

    def actionMLB(self):
        self.level = "mid"
        # Create a new game window
        self.game_window = GameWindow(16, 16, 40, 500, 500, 1000, 800, 800, 700, self, self.level)
        self.game_window.show()

        # Close this window
        self.win.close()

    def actionHLB(self):
        self.level = "hard"
        # Create a new game window
        self.game_window = GameWindow(16, 32, 80, 500, 500, 1600, 800, 1600, 800, self, self.level)
        self.game_window.show()

        # Close this window
        self.win.close()

    def actionCB(self):
        self.width_value = 8
        self.height_value = 8
        self.mines_value = 8
        self.custom_ui.setupUi(self.custom_win)
        self.custom_win.setWindowTitle("Custom")
        self.custom_win.show()
        self.custom_ui.widthPlusButton.clicked.connect(self.actionWPB)
        self.custom_ui.widthMinusButton.clicked.connect(self.actionWMB)
        self.custom_ui.heightPlusButton.clicked.connect(self.actionHPB)
        self.custom_ui.heightMinusButton.clicked.connect(self.actionHMB)
        self.custom_ui.minesPlusButton.clicked.connect(self.actionMPB)
        self.custom_ui.minesMinusButton.clicked.connect(self.actionMHB)
        self.custom_ui.playGameButton.clicked.connect(self.actionPGB)
        self.custom_ui.cancelButton.clicked.connect(self.actionCNB)

    def actionWPB(self):
        if self.width_value != 40:
            self.width_value += 1
            self.custom_ui.widthNumber.setProperty("intValue", self.width_value)

    def actionWMB(self):
        if self.width_value != 8:
            self.width_value -= 1
            self.custom_ui.widthNumber.setProperty("intValue", self.width_value)

    def actionHPB(self):
        if self.height_value != 40:
            self.height_value += 1
            self.custom_ui.heightNumber.setProperty("intValue", self.height_value)

    def actionHMB(self):
        if self.height_value != 8:
            self.height_value -= 1
            self.custom_ui.heightNumber.setProperty("intValue", self.height_value)

    def actionMPB(self):
        if self.mines_value != 200:
            self.mines_value += 1
            self.custom_ui.minesNumber.setProperty("intValue", self.mines_value)

    def actionMHB(self):
        if self.mines_value != 8:
            self.mines_value -= 1
            self.custom_ui.minesNumber.setProperty("intValue", self.mines_value)

    def actionPGB(self):
        self.level = "custom"
        self.game_window = GameWindow(self.width_value, self.height_value, self.mines_value, 500, 500, 1000, 800, 800, 700, self, self.level)
        self.game_window.show()

        self.custom_win.close()
        self.win.close()

    def actionCNB(self):
        self.custom_win.close()
