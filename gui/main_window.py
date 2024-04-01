from PySide6.QtWidgets import QMainWindow

from classes import Group, Participant
from gui.group_box_group import GroupBoxGroup
from gui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    groupBox: GroupBoxGroup
    groupBox_2: GroupBoxGroup
    groupBox_3: GroupBoxGroup

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setup_groups(
        self,
        participants: list[Participant],
        tries_per_route: int,
        groups: list[Group],
    ) -> None:
        assert len(groups) == 3
        boxes = {
            groups[0]: self.groupBox,
            groups[1]: self.groupBox_2,
            groups[2]: self.groupBox_3,
        }
        for grp in groups:
            box = boxes[grp]
            grp_participants = [x for x in participants if x.group == grp]
            box.setup_group(grp_participants, tries_per_route, grp.name, grp.routes)
