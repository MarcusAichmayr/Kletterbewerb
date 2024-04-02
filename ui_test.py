import sys

from PySide6.QtWidgets import QApplication

from classes import TRY_WEIGHTS
from gui.main_window import MainWindow
from set_data import groups, load_participants, save_participants


def save(participants, main_win: MainWindow) -> None:
    save_participants(participants)
    main_win.statusbar.showMessage("gespeichert", 4_000)


def main():
    participants = load_participants()
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.setup_groups(participants, len(TRY_WEIGHTS), groups)
    main_win.save_button.clicked.connect(lambda: save(participants, main_win))
    main_win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
