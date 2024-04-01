from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QSpinBox

from classes import Participant, Route


class GroupBoxGroup(QGroupBox):
    name: str
    tries_per_route: int
    routes: list[Route]
    grid_layout: QGridLayout
    heading_labels: list[QLabel]
    participant_labels: dict[Participant, QLabel]
    participant_res_labels: dict[Participant, QLabel]
    participant_try_inputs: dict[Participant, dict[Route, list[QSpinBox]]]

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setupUi(self)

    def setup_group(
        self,
        grp_participants: list[Participant],
        tries_per_route: int,
        grp_name: str,
        routes: list[Route],
    ) -> None:
        self.tries_per_route = tries_per_route
        self.name = grp_name
        self.routes = routes
        if not self.objectName():
            self.setObjectName("groupBoxGroup")
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setObjectName("gridLayout")
        self.setTitle(grp_name)
        self.setup_header()
        self.participant_labels = {}
        self.participant_res_labels = {}
        self.participant_try_inputs = {}
        for p in grp_participants:
            self.setup_participant(p)

    def setup_header(self) -> None:
        self.heading_labels = []

        col = 0
        lbl = QLabel(self)
        lbl.setObjectName(f"lbl_head_{col}")
        lbl.setText("Name")
        self.grid_layout.addWidget(lbl, 0, col, 1, 1)
        self.heading_labels.append(lbl)

        col = 1
        lbl = QLabel(self)
        lbl.setObjectName(f"lbl_head_{col}")
        lbl.setText("Ergebnis")
        self.grid_layout.addWidget(lbl, 0, col, 1, 1)
        self.heading_labels.append(lbl)

        for r in self.routes:
            col += 1
            lbl = QLabel(self)
            lbl.setObjectName(f"lbl_head_{self.name}_{col}")
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl.setText(f"{r.color} ({r.handholds})")
            self.grid_layout.addWidget(lbl, 0, col, 1, 1)
            self.heading_labels.append(lbl)
            # maybe add heading like "Versuch 1, Versuch 2, ..."

        line = QFrame(self)
        line.setObjectName("line")
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)

        self.grid_layout.addWidget(line, 1, 0, 1, self.grid_layout.columnCount())

    def setup_participant(self, participant: Participant) -> None:
        """add an participant to the group box

        Args:
            participant: the participant to add
        """
        row = self.grid_layout.rowCount() + 1
        col = 0
        lbl = QLabel(self)
        lbl.setObjectName(f"lbl_participant_{self.name}_{row}_{col}")
        lbl.setText(participant.name)
        self.grid_layout.addWidget(lbl, row, col, 1, 1)
        self.participant_labels[participant] = lbl

        col = 1
        lbl = QLabel(self)
        lbl.setObjectName(f"lbl_participant_{self.name}_{row}_{col}")
        lbl.setText(str(participant.result))
        self.grid_layout.addWidget(lbl, row, col, 1, 1)
        self.participant_res_labels[participant] = lbl

        self.participant_try_inputs[participant] = {}
        for r in self.routes:
            col += 1
            tries_layout = QHBoxLayout()
            tries_layout.setObjectName(f"tries_layout_{participant.name}_{row}_{col}")
            spin_boxes = []
            for t in range(self.tries_per_route):
                spin_box = QSpinBox(self)
                spin_box.setObjectName(f"tries_spin_box_{participant.name}_{row}_{col}_{t}")
                spin_box.setMaximum(r.handholds)
                spin_box.setValue(participant.points[r][t])
                spin_boxes.append(spin_box)
                tries_layout.addWidget(spin_box)
            self.participant_try_inputs[participant][r] = spin_boxes
            self.grid_layout.addLayout(tries_layout, row, col, 1, 1)
