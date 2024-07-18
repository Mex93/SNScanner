import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFontDatabase

import PySide6.QtCore as qc
import logging

from ui.untitled import Ui_MainWindow
from ui.config_project_menu import Ui_MainWindow as UI_ConfigWindow

from enums import CONFIG_MENU_FIELD_TYPE, WINDOW_TYPE
from common import send_message_box
from enums import SMBOX_ICON_TYPE, SN_COUNT_TYPE, FIELD_TYPE_ID, PROGRAM_STATUS, PROJECT_TYPE
from classes.CDB import CDatabase
from classes.CProject import CProject
from classes.CInputArea import CInputArea, CInputUnit, MAX_LOT_COUNT, MAX_FIELDS_ON_PAGE
from classes.CProjectWindow import CCreateWindow

# pyside6-uic .\ui\untitled.ui -o .\ui\untitled.py
# pyside6-rcc .\ui\res.qrc -o .\ui\res_rc.py
# Press the green button in the gutter to run the script.





class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__base_program_version = "0.1"  # Менять при каждом обновлении любой из подпрограмм
        self.__program_current_status: PROGRAM_STATUS = PROGRAM_STATUS.NO_PROJECT
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        self.setWindowTitle(f'SN Scan Квант 2024 v0.1')

        self.create_project_window = CCreateWindow(WINDOW_TYPE.CREATE, self)
        self.config_project_window = CCreateWindow(WINDOW_TYPE.CONFIG, self)

        self.db_unit = CDatabase()
        self.carea_unit = CInputArea()
        CInputUnit.set_main_window(main_window=self.ui)

        # connects
        # self.ui.pb_code.clicked.connect(self.on_user_clicked_convert_button)
        # self.ui.pb_decode.clicked.connect(self.on_user_clicked_deconvert_button)

        self.ui.pushButton_arrow_down.clicked.connect(self.on_user_press_down_btn)
        self.ui.pushButton_arrow_up.clicked.connect(self.on_user_press_up_btn)

        self.ui.action_new_project.triggered.connect(self.on_user_clicked_new_project)
        self.ui.action_set_parameters.triggered.connect(self.on_user_clicked_config_project)
        self.ui.action_open.triggered.connect(self.on_user_focus)
        self.set_program_to_default_state()

    def on_user_press_up_btn(self):
        self.carea_unit.set_down_page()

    def on_user_press_down_btn(self):
        self.carea_unit.set_next_page()

    def on_user_clicked_new_project(self):
        self.set_create_menu(True)

    def on_user_clicked_config_project(self):
        self.set_config_menu(True)

    def on_user_focus(self):
        handler: CDatabase = self.db_unit.connect_to_db("my_test")
        if handler:
            print(handler)
            self.db_unit.disconnect()

    def set_create_menu(self, status: bool):
        if status:
            self.create_project_window.show()
            self.create_project_window.setFocus()
        else:
            self.create_project_window.hide()

    def set_config_menu(self, status: bool):
        if status:
            self.config_project_window.show()
            self.config_project_window.setFocus()
        else:
            self.config_project_window.hide()

    def set_program_to_default_state(self):

        self.carea_unit.set_start()
        self.switch_program_status(PROGRAM_STATUS.NO_PROJECT)
        # self.carea_unit.set_field_data(5, FIELD_TYPE_ID.SN_2, "5TJKRJGIRWNJG")
        # for index in range(MAX_FIELDS_ON_PAGE):
        #     self.carea_unit.append_new_field_on_index()

        # self.carea_unit.set_field_data(2, FIELD_TYPE_ID.SN_2, "LOL")
        # self.carea_unit.set_field_data(5, FIELD_TYPE_ID.SN_3, "rwgjhwroijgrw")
        # print(self.carea_unit.get_field_data(5, FIELD_TYPE_ID.SN_3))
        #
        # print(self.carea_unit.delete_all_fields_in_line(5))
        #
        # print(self.carea_unit.insert_new_field_on_empty_place())
        # self.carea_unit.set_field_data(5, FIELD_TYPE_ID.SCAN_DATA, "egwe")
        #
        # print(f" удалено " + str(self.carea_unit.delete_all_fields_window()))

    def get_programm_status(self) -> PROGRAM_STATUS:
        return self.__program_current_status

    def switch_program_status(self, new_status: PROGRAM_STATUS) -> PROGRAM_STATUS:
        old = self.get_programm_status()
        if new_status == PROGRAM_STATUS.NO_PROJECT:
            self.ui.groupBox_main.setEnabled(False)
            self.ui.menu_2.setEnabled(False)  # полная блокировка меню настроек
            self.ui.action_saveas.setEnabled(False)
            self.ui.action_close.setEnabled(False)
            self.ui.verticalLayout_5.setEnabled(False)  # лайаут всего окна
            self.ui.pushButton_two_window.setEnabled(False)
            self.ui.frame.setEnabled(False)  # фрэйм кнопок вверх вниз
        elif new_status == PROGRAM_STATUS.IN_JOB:
            self.ui.groupBox_main.setEnabled(True)
            self.ui.menu_2.setEnabled(True)  # полная блокировка меню настроек
            self.ui.action_saveas.setEnabled(True)
            self.ui.action_close.setEnabled(True)
            self.ui.verticalLayout_5.setEnabled(True)  # лайаут всего окна
            self.ui.pushButton_two_window.setEnabled(True)
            self.ui.frame.setEnabled(True)  # фрэйм кнопок вверх вниз
        return old


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    logging.basicConfig(level=logging.DEBUG, filename="program.log", filemode="w")
    sys.exit(app.exec())
