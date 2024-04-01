# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QMainWindow, QMenuBar,
    QScrollArea, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

from gui.group_box_group import GroupBoxGroup

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(711, 564)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 691, 500))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = GroupBoxGroup(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = GroupBoxGroup(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = GroupBoxGroup(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.verticalLayout.addWidget(self.groupBox_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 711, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Jugend", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Kinder", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Mini", None))
    # retranslateUi

