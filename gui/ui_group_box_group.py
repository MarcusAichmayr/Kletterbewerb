# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'group_box_groupRZfFEK.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpinBox, QWidget)

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        if not GroupBox.objectName():
            GroupBox.setObjectName(u"GroupBox")
        GroupBox.resize(580, 300)
        self.gridLayout = QGridLayout(GroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(GroupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spinBox_7 = QSpinBox(GroupBox)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.horizontalLayout_3.addWidget(self.spinBox_7)

        self.spinBox_8 = QSpinBox(GroupBox)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.horizontalLayout_3.addWidget(self.spinBox_8)

        self.spinBox_9 = QSpinBox(GroupBox)
        self.spinBox_9.setObjectName(u"spinBox_9")

        self.horizontalLayout_3.addWidget(self.spinBox_9)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 3, 1, 1)

        self.label_5 = QLabel(GroupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label = QLabel(GroupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(GroupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox_4 = QSpinBox(GroupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.horizontalLayout_2.addWidget(self.spinBox_4)

        self.spinBox_5 = QSpinBox(GroupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.horizontalLayout_2.addWidget(self.spinBox_5)

        self.spinBox_6 = QSpinBox(GroupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.horizontalLayout_2.addWidget(self.spinBox_6)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 2, 1, 1)

        self.label_4 = QLabel(GroupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinBox = QSpinBox(GroupBox)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)

        self.spinBox_2 = QSpinBox(GroupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.horizontalLayout.addWidget(self.spinBox_2)

        self.spinBox_3 = QSpinBox(GroupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.horizontalLayout.addWidget(self.spinBox_3)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)


        self.retranslateUi(GroupBox)

        QMetaObject.connectSlotsByName(GroupBox)
    # setupUi

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(QCoreApplication.translate("GroupBox", u"GroupBox", None))
        GroupBox.setTitle(QCoreApplication.translate("GroupBox", u"Jugend", None))
        self.label_3.setText(QCoreApplication.translate("GroupBox", u"Route 2", None))
        self.label_5.setText(QCoreApplication.translate("GroupBox", u"John", None))
        self.label.setText(QCoreApplication.translate("GroupBox", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("GroupBox", u"Route 1", None))
        self.label_4.setText(QCoreApplication.translate("GroupBox", u"Route 3", None))
    # retranslateUi

