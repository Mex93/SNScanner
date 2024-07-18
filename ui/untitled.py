# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1582, 880)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1442, 0))
        icon = QIcon()
        icon.addFile(u":/res/images/logo.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.action_new_project = QAction(MainWindow)
        self.action_new_project.setObjectName(u"action_new_project")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_close = QAction(MainWindow)
        self.action_close.setObjectName(u"action_close")
        self.action_set_parameters = QAction(MainWindow)
        self.action_set_parameters.setObjectName(u"action_set_parameters")
        self.action_set_default_parameters = QAction(MainWindow)
        self.action_set_default_parameters.setObjectName(u"action_set_default_parameters")
        self.action_saveas = QAction(MainWindow)
        self.action_saveas.setObjectName(u"action_saveas")
        self.action_11 = QAction(MainWindow)
        self.action_11.setObjectName(u"action_11")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_instruction = QAction(MainWindow)
        self.action_instruction.setObjectName(u"action_instruction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_tv_name = QLabel(self.centralwidget)
        self.label_tv_name.setObjectName(u"label_tv_name")
        font = QFont()
        font.setPointSize(20)
        self.label_tv_name.setFont(font)
        self.label_tv_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_tv_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_two_window = QPushButton(self.centralwidget)
        self.pushButton_two_window.setObjectName(u"pushButton_two_window")
        icon1 = QIcon()
        icon1.addFile(u":/res/images/select_window_open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_two_window.setIcon(icon1)
        self.pushButton_two_window.setIconSize(QSize(40, 40))
        self.pushButton_two_window.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_two_window)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_main = QGroupBox(self.centralwidget)
        self.groupBox_main.setObjectName(u"groupBox_main")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_main)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_sn2 = QLabel(self.groupBox_main)
        self.label_sn2.setObjectName(u"label_sn2")
        self.label_sn2.setFont(font)
        self.label_sn2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_sn2, 0, 2, 1, 1)

        self.label_result = QLabel(self.groupBox_main)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setFont(font)
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_result, 0, 6, 1, 1)

        self.horizontalSpacer_header_delitel = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_header_delitel, 0, 4, 1, 1)

        self.label_sn3 = QLabel(self.groupBox_main)
        self.label_sn3.setObjectName(u"label_sn3")
        self.label_sn3.setFont(font)
        self.label_sn3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_sn3, 0, 3, 1, 1)

        self.label_sn1 = QLabel(self.groupBox_main)
        self.label_sn1.setObjectName(u"label_sn1")
        self.label_sn1.setFont(font)
        self.label_sn1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_sn1, 0, 1, 1, 1)

        self.label_data = QLabel(self.groupBox_main)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setFont(font)
        self.label_data.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_data.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_data, 0, 5, 1, 1)

        self.label_number = QLabel(self.groupBox_main)
        self.label_number.setObjectName(u"label_number")
        self.label_number.setFont(font)
        self.label_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_number, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.groupBox_main)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_arrow_up = QPushButton(self.frame)
        self.pushButton_arrow_up.setObjectName(u"pushButton_arrow_up")
        icon2 = QIcon()
        icon2.addFile(u":/res/images/arrow_up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_arrow_up.setIcon(icon2)
        self.pushButton_arrow_up.setIconSize(QSize(40, 40))
        self.pushButton_arrow_up.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_arrow_up)

        self.pushButton_arrow_down = QPushButton(self.frame)
        self.pushButton_arrow_down.setObjectName(u"pushButton_arrow_down")
        icon3 = QIcon()
        icon3.addFile(u":/res/images/arrow_down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_arrow_down.setIcon(icon3)
        self.pushButton_arrow_down.setIconSize(QSize(40, 40))
        self.pushButton_arrow_down.setFlat(True)

        self.verticalLayout.addWidget(self.pushButton_arrow_down)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 2)

        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1582, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menuBar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action_new_project)
        self.menu.addSeparator()
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_close)
        self.menu.addSeparator()
        self.menu.addAction(self.action_saveas)
        self.menu_2.addAction(self.action_set_parameters)
        self.menu_2.addAction(self.action_set_default_parameters)
        self.menu_3.addAction(self.action_about)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_instruction)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SNScanner", None))
        self.action_new_project.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_close.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.action_set_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.action_set_default_parameters.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.action_saveas.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0444\u0438\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0432\u0438\u0434", None))
        self.action_11.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043b\u043e\u0442\u0435", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action_instruction.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.label_tv_name.setText(QCoreApplication.translate("MainWindow", u"TV NAME", None))
        self.pushButton_two_window.setText("")
        self.groupBox_main.setTitle(QCoreApplication.translate("MainWindow", u"CFields", None))
        self.label_sn2.setText(QCoreApplication.translate("MainWindow", u"SN2:", None))
        self.label_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        self.label_sn3.setText(QCoreApplication.translate("MainWindow", u"SN3:", None))
        self.label_sn1.setText(QCoreApplication.translate("MainWindow", u"SN1:", None))
        self.label_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
        self.label_number.setText(QCoreApplication.translate("MainWindow", u"\u2116:", None))
        self.pushButton_arrow_up.setText("")
        self.pushButton_arrow_down.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0435\u043a\u0442", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
    # retranslateUi

