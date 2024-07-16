from enums import FIELD_INDEX_ARR_TYPE
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QMainWindow, QMenu,
                               QMenuBar, QPushButton, QScrollArea, QSizePolicy,
                               QSpacerItem, QVBoxLayout, QWidget)
from ui.untitled import Ui_MainWindow

from enums import FIELD_TYPE_ID


class CInputUnit:
    main_window = None
    field_index = 0

    def __init__(self, field_id: FIELD_TYPE_ID, field_index: int):
        self.__field_type_id = field_id
        self.__field_index = field_index

    def get_field_index(self):
        return self.__field_index

    @classmethod
    def set_field_index(cls):
        cls.field_index += 1

    @classmethod
    def set_main_window(cls, mw: main_window):
        cls.main_window = mw

    @classmethod
    def get_main_window(cls):
        return cls.main_window

    def get_field_type(self):
        return self.__field_type_id

    def create_field_unit(self, data: str):
        main_window = self.get_main_window()
        if main_window:
            lineEdit_sn1_0 = QLineEdit(main_window.scrollAreaWidgetContents)
            lineEdit_sn1_0.setObjectName(u"lineEdit_sn1_0")
        else:
            raise ValueError("Main Menu is None in CInputUnit")


class CInputArea:
    __list_of_input = list()

    def __init__(self, main_window: Ui_MainWindow):
        self.__mw = main_window

    def get_all_fields(self):
        return self.__list_of_input

    def append_new_field(self, sql_index: int):
        self.__list_of_input.append(["", "", "", "", False, sql_index])

    def set_field_data(self, field_index: int, pod_index: int, data: any):

        if data not in (str, bool):
            raise TypeError("Data is not bool and not string")

        if field_index < 0 or len(self.__list_of_input) < field_index:
            raise IndexError("Invalid Field Index")

        if pod_index < 0 or len(self.__list_of_input[field_index]) < pod_index:
            raise IndexError("Invalid Pod Index")

        self.__list_of_input[field_index][pod_index] = data
