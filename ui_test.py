import sys
from threading import Thread
from time import sleep

from PySide6.QtWidgets import QApplication

from classes import TRY_WEIGHTS
from gui.main_window import MainWindow
from set_data import groups, save_participants, load_participants


def save(participants, main_win: MainWindow) -> None:
    save_participants(participants)
    th = Thread(
        target=show_status_message,
        kwargs=dict(message="gespeichert", status_bar=main_win.statusbar, duration=4.0),
    )
    th.start()


def show_status_message(*, message: str, status_bar, duration: float):
    status_bar.showMessage(message)
    sleep(duration)
    if status_bar.currentMessage() == message:
        status_bar.clearMessage()


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
