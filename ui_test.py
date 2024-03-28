import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
