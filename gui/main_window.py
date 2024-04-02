from PySide6.QtCore import QRect
from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QHBoxLayout,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from classes import Group, Participant
from gui.group_box_group import GroupBoxGroup


class MainWindow(QMainWindow):
    verticalLayout: QVBoxLayout
    groupBox: GroupBoxGroup
    groupBox_2: GroupBoxGroup
    groupBox_3: GroupBoxGroup
    group_boxes: dict[Group, GroupBoxGroup]

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self) -> None:
        self.setWindowTitle("Kletterbewerb")
        if not self.objectName():
            self.setObjectName("MainWindow")
        self.resize(750, 600)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 691, 500))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.save_button.setText("Speichern")

        self.horizontalLayout.addWidget(self.save_button)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 711, 22))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def setup_groups(
        self,
        participants: list[Participant],
        tries_per_route: int,
        groups: list[Group],
    ) -> None:
        boxes: dict[Group, GroupBoxGroup] = {}
        for grp in groups:
            grp_box = GroupBoxGroup(self.scrollAreaWidgetContents)
            grp_box.setObjectName(f"group_box_group_{grp.name}")
            self.verticalLayout.addWidget(grp_box)
            boxes[grp] = grp_box
        for grp in groups:
            box = boxes[grp]
            grp_participants = [x for x in participants if x.group == grp]
            box.setup_group(grp_participants, tries_per_route, grp.name, grp.routes)
        self.group_boxes = boxes
