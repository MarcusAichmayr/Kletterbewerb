from PySide6.QtWidgets import QGroupBox

from gui.ui_group_box_group import Ui_GroupBox


class GroupBoxGroup(QGroupBox, Ui_GroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
