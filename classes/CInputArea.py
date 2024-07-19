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

from classes.CProject import CProject
from enums import FIELD_TYPE_ID, FIELD_TYPE, SN_COUNT_TYPE, CONFIG_MENU_FIELD_TYPE
from common import get_current_data_stamp_ex

MAX_LOT_COUNT = 100
MIN_LOT_COUNT = 20
MAX_FIELDS_ON_PAGE = 20
TEXT_ON_RESULT_FIELD = "OK"


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

    def get_data(self) -> None | str:
        """Что хранится в AREA или Лэйбле"""
        if self.__widjet_unit:
            if self.__field_type in (FIELD_TYPE.INPUT_AREA, FIELD_TYPE.TEXT_LABEL):
                unit: QLabel | QLineEdit = self.__widjet_unit
                return str(unit.text())
        return None

    def set_data(self, data: str) -> None | bool:
        """Задать данные в лэйбл или ареу"""
        if self.__widjet_unit:
            if self.__field_type in (FIELD_TYPE.INPUT_AREA, FIELD_TYPE.TEXT_LABEL):
                unit: QLabel | QLineEdit = self.__widjet_unit
                unit.setText(data)
                return True
        return None

    def get_widjet_unit(self):
        return self.__widjet_unit

    def create_field_unit(self) -> bool:
        main_window = self.__main_window
        if main_window:

            font1 = QFont()
            font1.setPointSize(14)

            table_index = self.__table_index
            if self.__field_type_id == FIELD_TYPE_ID.NUMBER_LABEL:

                font = QFont()
                font.setPointSize(20)

                unit = QLabel(main_window.groupBox_main)
                unit.setFont(font)
                unit.setText(QCoreApplication.translate("MainWindow", f"{str(table_index + 1)}", None))
                main_window.gridLayout.addWidget(unit, table_index + 1, self.__field_in_line_index, 1, 1)

                self.__widjet_unit = unit
                self.__field_type = FIELD_TYPE.TEXT_LABEL
                return True

            elif self.__field_type_id in (FIELD_TYPE_ID.SN_1, FIELD_TYPE_ID.SN_2, FIELD_TYPE_ID.SN_3):

                unit = QLineEdit(main_window.groupBox_main)

                sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)
                sizePolicy1.setHeightForWidth(unit.sizePolicy().hasHeightForWidth())

                unit.setSizePolicy(sizePolicy1)
                unit.setMinimumSize(QSize(400, 0))
                unit.setFont(font1)
                unit.setAlignment(Qt.AlignmentFlag.AlignCenter)
                unit.setClearButtonEnabled(True)

                main_window.gridLayout.addWidget(unit, table_index + 1, self.__field_in_line_index, 1, 1)
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

                unit = QLineEdit(main_window.groupBox_main)
                unit.setFont(font1)
                unit.setFrame(False)
                unit.setAlignment(Qt.AlignmentFlag.AlignCenter)
                unit.setReadOnly(True)

                main_window.gridLayout.addWidget(unit, table_index + 1, self.__field_in_line_index, 1, 1)
                self.__widjet_unit = unit
                self.__field_type = FIELD_TYPE.INPUT_AREA
                return True

            elif self.__field_type_id == FIELD_TYPE_ID.RESULT_STATUS:
                unit = QLineEdit(main_window.groupBox_main)
                unit.setFont(font1)
                unit.setFrame(False)
                unit.setDragEnabled(False)
                unit.setReadOnly(True)
                unit.setAlignment(Qt.AlignmentFlag.AlignCenter)
                unit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
                unit.setClearButtonEnabled(False)

                main_window.gridLayout.addWidget(unit, table_index + 1, self.__field_in_line_index, 1, 1)
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
    for index in range(MAX_LOT_COUNT):
        __list_of_input.append([index, None])

    __main_window: Ui_MainWindow = None
    __table_index = 0
    __current_page = 1

    @classmethod
    def set_start(cls):
        cls.set_next_page()

    @classmethod
    def set_main_window(cls, mwindow: Ui_MainWindow):
        cls.__main_window = mwindow

    @classmethod
    def get_main_window(cls) -> Ui_MainWindow:
        return cls.__main_window

    @classmethod
    def set_name_for_labels(cls):
        sn1 = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_ONE)
        sn2 = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_TWO)
        sn3 = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_TRI)
        project_name = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.PROJECT_NAME)
        sns_count = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.SNS_COUNT)
        mw = cls.get_main_window()

        mw.label_sn1.setText(sn1)
        mw.label_sn2.setText(sn2)
        mw.label_sn3.setText(sn3)
        mw.label_tv_name.setText(project_name)

        if sns_count == SN_COUNT_TYPE.SN_DOUBLE:
            mw.label_sn3.hide()
        elif sns_count == SN_COUNT_TYPE.SN_TRIPLE:
            mw.label_sn3.show()



    @classmethod
    def set_down_page(cls):
        if cls.__table_index > MAX_FIELDS_ON_PAGE:
            cls.delete_fields()
            cls.__current_page -= 1

            cls.__table_index -= MAX_FIELDS_ON_PAGE * 2
            if cls.__table_index < 0:
                cls.__table_index = 0
            cls.set_render_fields()

    @classmethod
    def set_next_page(cls):
        lot_count = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.LOT_COUNT)
        if cls.__table_index < lot_count:
            cls.delete_fields()
            cls.__current_page += 1

            tindex = cls.__table_index
            result = lot_count - tindex
            if result < MAX_FIELDS_ON_PAGE:
                cls.__table_index = lot_count - MAX_FIELDS_ON_PAGE

            cls.set_render_fields()

    @classmethod
    def set_render_fields(cls) -> int | None:

        fields = [
            FIELD_TYPE_ID.NUMBER_LABEL,
            FIELD_TYPE_ID.SN_1,
            FIELD_TYPE_ID.SN_2]

        if CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.SNS_COUNT) == SN_COUNT_TYPE.SN_TRIPLE:
            fields.append(FIELD_TYPE_ID.SN_3)
        fields.append(
            # FIELD_TYPE_ID.HORIZONTAL_SPACER,
            FIELD_TYPE_ID.SCAN_DATA)
        fields.append(
            FIELD_TYPE_ID.RESULT_STATUS)

        for index in range(MAX_FIELDS_ON_PAGE):

            tindex = cls.__table_index
            print(tindex, CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.LOT_COUNT))
            if tindex >= CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.LOT_COUNT):
                return
            unit_list = list()

            for ftype in fields:
                field_unit = CInputUnit(ftype, tindex)
                if not field_unit.create_field_unit():
                    raise RuntimeError("Error in render fields")
                unit_list.append(field_unit)

                if ftype in (FIELD_TYPE_ID.SN_1, FIELD_TYPE_ID.SN_2, FIELD_TYPE_ID.SN_3):
                    widjet = field_unit.get_widjet_unit()
                    if widjet:
                        widjet.textChanged.connect(lambda fid=ftype, unit=field_unit:
                                                   cls.on_user_text_changed_in_field(fid, unit))

            cls.__list_of_input[tindex] = [tindex, unit_list]
            cls.__table_index += 1

    @classmethod
    # field_id не ошибка, по какой то пока не известной мне причине за место field id передаётся datas вообще из тела
    def on_user_text_changed_in_field(cls, field_id: FIELD_TYPE_ID, field_unit: CInputUnit):
        datas = field_unit.get_data()
        index = field_unit.get_field_table_index()
        field_id = field_unit.get_field_type_id()

        units_in_line = cls.get_units_in_line(index)

        if units_in_line is not None:
            max_index = 0

            check_list = [FIELD_TYPE_ID.SN_1, FIELD_TYPE_ID.SN_2]
            sns_count = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.SNS_COUNT)
            if sns_count == SN_COUNT_TYPE.SN_TRIPLE:
                max_index = 2
                check_list.append(FIELD_TYPE_ID.SN_3)
            else:
                max_index = 1

            sns_result = []

            for unit in units_in_line:
                if unit.get_field_type_id() in check_list:
                    sns_result.append(unit.get_data())

            is_any_text = False
            for item in sns_result:
                if item != '':
                    is_any_text = True
                    break

            result_unit = cls.get_unit(units_in_line, FIELD_TYPE_ID.RESULT_STATUS)
            date_unit = cls.get_unit(units_in_line, FIELD_TYPE_ID.SCAN_DATA)
            widjet = result_unit.get_widjet_unit()

            if sns_result[0] == sns_result[1] == sns_result[max_index] and sns_result[0]:
                result_unit.set_data(TEXT_ON_RESULT_FIELD)
                widjet.setStyleSheet(u"background: green")
                cdate = get_current_data_stamp_ex()
                date_unit.set_data(cdate)
            else:
                if not is_any_text:
                    widjet.setStyleSheet('')
                else:
                    widjet.setStyleSheet(u"background: red")
                result_unit.set_data("")
                date_unit.set_data("")

        print(index, field_id, datas)

    @classmethod
    def get_unit(cls, units, ftype: FIELD_TYPE_ID) -> CInputUnit | None:
        for unit_find in units:
            if unit_find.get_field_type_id() == ftype:
                return unit_find

    @classmethod
    def get_units_in_line(cls, table_index: int) -> list[CInputUnit] | None:
        if cls.is_valid_table_index(table_index):
            return cls.__list_of_input[table_index][1]

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
    def get_current_table_index(cls) -> int:
        return cls.__table_index

    @classmethod
    def get_current_page(cls) -> int:
        return cls.__current_page

    def get_all_fields(self):
        return self.__list_of_input

    @classmethod
    def is_valid_table_index(cls, table_index: int) -> bool:
        if 0 <= table_index < len(cls.__list_of_input):
            if isinstance(cls.__list_of_input[table_index], list):  # if cls.__list_of_input[table_index] is not None:
                return True
        return False

    @classmethod
    def get_field_data(cls, table_index: int, field_id: FIELD_TYPE_ID) -> bool | str:
        if cls.is_valid_table_index(table_index):
            units = cls.__list_of_input[table_index][1]
            if isinstance(units, list):
                unit = cls.get_unit(units, field_id)
                if unit:
                    return unit.get_data()
        return False

    @classmethod
    def set_field_data(cls, table_index: int, field_id: FIELD_TYPE_ID, data: str) -> bool | str:
        if cls.is_valid_table_index(table_index):
            units = cls.__list_of_input[table_index][1]
            if isinstance(units, list):
                unit = cls.get_unit(units, field_id)
                if unit:
                    unit.set_data(data)
                    return True
        return False

    @classmethod
    def get_empty_field_place(cls):
        for index in range(len(cls.__list_of_input)):
            if cls.__list_of_input[index][1] is None:
                return index
        return -1

    @classmethod
    def is_field_empty(cls, table_index: int):
        if 0 <= table_index < len(cls.__list_of_input):
            if cls.__list_of_input[table_index][1] is None:  # if isinstance(cls.__list_of_input[table_index], list):
                return True
            else:
                return False
        return False

    @classmethod
    def delete_fields(cls) -> int:

        count = 0
        tindex = cls.__table_index
        if tindex <= 0:
            return 0
        for index in range(tindex - MAX_FIELDS_ON_PAGE, tindex):
            tindex = cls.__list_of_input[index][0]
            units_list = cls.__list_of_input[index][1]

            if not isinstance(units_list, list):
                continue

            result = 0
            for unit in units_list:
                if isinstance(unit, CInputUnit):
                    unit.delete_unit()
                    result += 1

            if result > 0:
                cls.__list_of_input[index][1] = None
                count += 1

        return count
