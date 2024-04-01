import sys

from PySide6.QtWidgets import QApplication

from classes import TRY_WEIGHTS
from gui.main_window import MainWindow
from set_data import groups, participants

def main():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.setup_groups(participants, len(TRY_WEIGHTS), groups)
    main_win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
