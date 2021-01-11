import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Initialize setup window
    window = MainWindow()
    window.show()
    # Run QT App
    app.exec_()
