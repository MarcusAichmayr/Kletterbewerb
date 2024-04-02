import sys

from PySide6.QtWidgets import QApplication

from classes import TRY_WEIGHTS
from gui.main_window import MainWindow
from set_data import groups, participants_from_json, save_participants


def main():
    participants = participants_from_json()
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.setup_groups(participants, len(TRY_WEIGHTS), groups)
    main_win.save_button.clicked.connect(lambda: save_participants(participants))
    main_win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
