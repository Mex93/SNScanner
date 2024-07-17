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

from enums import FIELD_TYPE_ID, FIELD_TYPE


class CInputUnit:
    """Класс хранящий виджет и его параметры и манипуляции
    table_index у виджета должен быть всегда +1 от индекса списка юнитов виджетов
    """
    __main_window = None

    def __init__(self, field_id: FIELD_TYPE_ID, table_index: int):

        self.__table_index = table_index
        self.__field_in_line_index = CInputArea.get_field_place_in_line(field_id)

        self.__field_type_id: FIELD_TYPE_ID = field_id
        self.__field_type: FIELD_TYPE | None = None

        self.__widjet_unit: QLabel | QLineEdit | None = None

    @classmethod
    def set_main_window(cls, main_window: Ui_MainWindow):
        cls.__main_window = main_window

    def get_in_line_index(self) -> int:
        """Индекс порядковый в линии"""
        return self.__field_in_line_index

    def get_field_type(self) -> FIELD_TYPE | None:
        """Тип поля - СПАСЕР АРЕА ЛЭЙБЛ"""
        return self.__field_type

    def get_field_type_id(self) -> FIELD_TYPE_ID:
        """Как порядковый номер элемента в строке"""
        return self.__field_type_id

    def get_field_table_index(self) -> int:
        """Порядковый номер столбца кучки лейблов"""
        return self.__table_index

    def get_field_data(self) -> None | str:
        """Что хранится в AREA или Лэйбле"""
        if self.__widjet_unit:
            if self.__field_type in (FIELD_TYPE.INPUT_AREA, FIELD_TYPE.TEXT_LABEL):
                unit: QLabel | QLineEdit = self.__widjet_unit
                return str(unit.text())
        return None

    def set_field_data(self, data: str) -> None | bool:
        """Задать данные в лэйбл или ареу"""
        if self.__widjet_unit and data:
            if self.__field_type in (FIELD_TYPE.INPUT_AREA, FIELD_TYPE.TEXT_LABEL):
                unit: QLabel | QLineEdit = self.__widjet_unit
                unit.setText(data)
                return True
        return None

    def create_field_unit(self) -> bool:
        main_window = self.__main_window
        if main_window:

            font1 = QFont()
            font1.setPointSize(14)

            table_index = self.__table_index
            if self.__field_type_id == FIELD_TYPE_ID.NUMBER_LABEL:

                font = QFont()
                font.setPointSize(20)

                unit = QLabel(main_window.scrollAreaWidgetContents)
                unit.setFont(font)
                unit.setText(QCoreApplication.translate("MainWindow", f"{str(table_index+1)}", None))
                main_window.gridLayout.addWidget(unit, table_index+1, self.__field_in_line_index, 1, 1)

                self.__widjet_unit = unit
                self.__field_type = FIELD_TYPE.TEXT_LABEL
                return True

            elif self.__field_type_id in (FIELD_TYPE_ID.SN_1, FIELD_TYPE_ID.SN_2, FIELD_TYPE_ID.SN_3):

                unit = QLineEdit(main_window.scrollAreaWidgetContents)

                sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)
                sizePolicy1.setHeightForWidth(unit.sizePolicy().hasHeightForWidth())

                unit.setSizePolicy(sizePolicy1)
                unit.setMinimumSize(QSize(400, 0))
                unit.setFont(font1)
                unit.setAlignment(Qt.AlignmentFlag.AlignCenter)
                unit.setClearButtonEnabled(True)

                main_window.gridLayout.addWidget(unit, table_index+1, self.__field_in_line_index, 1, 1)
                # self.gridLayout.addWidget(self.lineEdit_sn2_0, 1, 2, 1, 1)
                # self.gridLayout.addWidget(self.lineEdit_sn3_0, 1, 3, 1, 1)

                self.__widjet_unit = unit
                self.__field_type = FIELD_TYPE.INPUT_AREA
                return True

            if self.__field_type_id == FIELD_TYPE_ID.HORIZONTAL_SPACER:

                # unit = QSpacerItem(18, 18, QSizePolicy.Policy.Expanding,
                #                    QSizePolicy.Policy.Minimum)
                # main_window.gridLayout.addItem(unit, table_index, self.__field_in_line_index, 1, 1)
                #
                # self.__widjet_unit = unit
                # self.__field_type = FIELD_TYPE.SPACER
                return False
            elif self.__field_type_id == FIELD_TYPE_ID.SCAN_DATA:

                unit = QLineEdit(main_window.scrollAreaWidgetContents)
                unit.setFont(font1)
                unit.setFrame(False)
                unit.setReadOnly(True)

                main_window.gridLayout.addWidget(unit, table_index+1, self.__field_in_line_index, 1, 1)
                self.__widjet_unit = unit
                self.__field_type = FIELD_TYPE.INPUT_AREA
                return True

            elif self.__field_type_id == FIELD_TYPE_ID.RESULT_STATUS:
                unit = QLineEdit(main_window.scrollAreaWidgetContents)
                unit.setFont(font1)
                unit.setFrame(False)
                unit.setDragEnabled(False)
                unit.setReadOnly(True)
                unit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
                unit.setClearButtonEnabled(False)

                main_window.gridLayout.addWidget(unit, table_index+1, self.__field_in_line_index, 1, 1)
                self.__widjet_unit = unit
                self.__field_type = FIELD_TYPE.INPUT_AREA

                return True
            else:
                raise ValueError("Invalid Field Place")
        else:
            raise ValueError("Main Menu is None in CInputUnit")

    def delete_unit(self):
        if self.__widjet_unit:
            if self.__field_type == FIELD_TYPE.INPUT_AREA:
                self.__widjet_unit.deleteLater()
            elif self.__field_type == FIELD_TYPE.TEXT_LABEL:
                self.__widjet_unit.deleteLater()
            elif self.__field_type == FIELD_TYPE.SPACER:
                pass
            self.__widjet_unit = None
            del self


class CInputArea:
    """
    Класс для обработки строк

    Spacer не задействован так как оказывается достаточно одного в колонке"""
    __list_of_input = list()
    __table_index = -1

    @classmethod
    def get_field_place_in_line(cls, field_id: FIELD_TYPE_ID):
        if field_id == FIELD_TYPE_ID.NUMBER_LABEL:
            return 0
        elif field_id == FIELD_TYPE_ID.SN_1:
            return 1
        elif field_id == FIELD_TYPE_ID.SN_2:
            return 2
        elif field_id == FIELD_TYPE_ID.SN_3:
            return 3
        elif field_id == FIELD_TYPE_ID.HORIZONTAL_SPACER:
            return 4
        elif field_id == FIELD_TYPE_ID.SCAN_DATA:
            return 5
        elif field_id == FIELD_TYPE_ID.RESULT_STATUS:
            return 6
        else:
            raise ValueError("Error in field ID")

    @classmethod
    def set_field_index(cls) -> int:
        cls.__table_index += 1
        return cls.__table_index

    def get_all_fields(self):
        return self.__list_of_input

    @classmethod
    def is_valid_table_index(cls, table_index: int) -> bool:
        if 0 <= table_index < len(cls.__list_of_input):
            if isinstance(cls.__list_of_input[table_index], list):
                return True
        return False

    @classmethod
    def get_field_data(cls, table_index: int, field_id: FIELD_TYPE_ID) -> bool | str:
        if cls.is_valid_table_index(table_index):
            field_list_of_units = cls.__list_of_input[table_index]
            if isinstance(field_list_of_units[field_id], CInputUnit):
                field_unit: CInputUnit = field_list_of_units[field_id]
                return field_unit.get_field_data()
        return False

    @classmethod
    def set_field_data(cls, table_index: int, field_id: FIELD_TYPE_ID, data: str) -> bool | str:
        if cls.is_valid_table_index(table_index):
            field_list_of_units = cls.__list_of_input[table_index]
            if isinstance(field_list_of_units[field_id], CInputUnit):
                field_unit: CInputUnit = field_list_of_units[field_id]
                if field_unit.set_field_data(data):
                    return True
        return False

    @classmethod
    def append_new_field_on_index(cls, insert_table_index=None) -> bool:

        if insert_table_index is None:
            table_index = cls.set_field_index()
        else:
            if not cls.is_field_empty(insert_table_index):
                return False

            table_index = insert_table_index

        unit_list = list()

        fields = [
            FIELD_TYPE_ID.NUMBER_LABEL,
            FIELD_TYPE_ID.SN_1,
            FIELD_TYPE_ID.SN_2,
            FIELD_TYPE_ID.SN_3,
            # FIELD_TYPE_ID.HORIZONTAL_SPACER,
            FIELD_TYPE_ID.SCAN_DATA,
            FIELD_TYPE_ID.RESULT_STATUS
        ]

        for ftype in fields:
            field_unit = CInputUnit(ftype, table_index)
            if not field_unit.create_field_unit():
                raise RuntimeError("Error in render fields")
            unit_list.append(field_unit)

        if insert_table_index is None:
            cls.__list_of_input.append(unit_list)
            return True
        else:
            cls.__list_of_input = unit_list
            return True

    @classmethod
    def get_empty_field_place(cls):
        for index in range(len(cls.__list_of_input)):
            if cls.__list_of_input[index] is None:
                return index
        return -1

    @classmethod
    def is_field_empty(cls, table_index: int):
        if 0 <= table_index < len(cls.__list_of_input):
            if isinstance(cls.__list_of_input[table_index], list):
                return False
            else:
                return True
        return False

    @classmethod
    def insert_new_field_on_empty_place(cls) -> bool:
        empty_index = cls.get_empty_field_place()
        if empty_index == -1:
            return cls.append_new_field_on_index()
        else:
            return cls.append_new_field_on_index(empty_index)

    @classmethod
    def delete_all_fields_in_line(cls, table_index: int) -> bool:

        if cls.is_valid_table_index(table_index):
            field_list_of_units = cls.__list_of_input[table_index]
            result = 0
            for unit in field_list_of_units:
                if isinstance(unit, CInputUnit):
                    unit.delete_unit()
                    result += 1
            if result > 0:
                print(table_index)
                cls.__list_of_input[table_index] = None
                return True

        return False

    @classmethod
    def delete_all_fields_window(cls) -> int:

        count = 0
        for index in range(len(cls.__list_of_input)):
            if cls.delete_all_fields_in_line(index):
                count += 1
        if count > 0:
            cls.__list_of_input = []
        return count
