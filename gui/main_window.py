from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QMainWindow,
    QMenuBar,
    QScrollArea,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from classes import Group, Participant
from gui.group_box_group import GroupBoxGroup
from gui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    verticalLayout: QVBoxLayout
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
        boxes: dict[Group, GroupBoxGroup] = {}
        if len(groups) == 3:
            boxes = {
                groups[0]: self.groupBox,
                groups[1]: self.groupBox_2,
                groups[2]: self.groupBox_3,
            }
        else:
            self.verticalLayout.removeWidget(self.groupBox)
            self.verticalLayout.removeWidget(self.groupBox_2)
            self.verticalLayout.removeWidget(self.groupBox_3)
            for grp in groups:
                grp_box = GroupBoxGroup(self.scrollAreaWidgetContents)
                grp_box.setObjectName(f"group_box_group_{grp.name}")
                self.verticalLayout.addWidget(grp_box)
                boxes[grp] = grp_box
        for grp in groups:
            box = boxes[grp]
            grp_participants = [x for x in participants if x.group == grp]
            box.setup_group(grp_participants, tries_per_route, grp.name, grp.routes)
