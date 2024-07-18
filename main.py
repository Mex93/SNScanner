import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFontDatabase

import PySide6.QtCore as qc

from ui.untitled import Ui_MainWindow
from ui.config_project_menu import Ui_MainWindow as UI_ConfigWindow

from enums import CONFIG_MENU_FIELD_TYPE, WINDOW_TYPE
from common import send_message_box
from enums import SMBOX_ICON_TYPE, SN_COUNT_TYPE, FIELD_TYPE_ID, PROGRAM_STATUS, PROJECT_TYPE
from classes.CDB import CDatabase
from classes.CProject import CProject
from classes.CInputArea import CInputArea, CInputUnit, MAX_LOT_COUNT, MAX_FIELDS_ON_PAGE


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


class CCreateWindow(QMainWindow):
    def __init__(self, window_type: WINDOW_TYPE, main_window: MainWindow, parent=None):
        super().__init__(parent)
        self.window_type = window_type
        self.__main_window = main_window
        self.ui = UI_ConfigWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        if window_type == WINDOW_TYPE.CREATE:
            self.setWindowTitle(f'Создать проект')
            self.ui.pushButton_save.setText("Создать")
        elif window_type == WINDOW_TYPE.CONFIG:
            self.setWindowTitle(f'Настройки проекта')
            self.ui.pushButton_save.setText("Сохранить")

        self.set_default_all_fields()
        self.setWindowModality(qc.Qt.WindowModality.ApplicationModal)

        # connects
        # self.ui.pb_code.clicked.connect(self.on_user_clicked_convert_button)
        # self.ui.pb_decode.clicked.connect(self.on_user_clicked_deconvert_button)

        self.ui.pushButton_save.clicked.connect(self.on_user_pressed_save_create)
        self.ui.pushButton_set_default.clicked.connect(self.on_user_pressed_default)

        self.ui.lineEdit_sn1.textEdited.connect(
            lambda: self.on_user_input_text(CONFIG_MENU_FIELD_TYPE.SN_ONE, self.ui.lineEdit_sn1))
        self.ui.lineEdit_sn2.textEdited.connect(
            lambda: self.on_user_input_text(CONFIG_MENU_FIELD_TYPE.SN_TWO, self.ui.lineEdit_sn2))
        self.ui.lineEdit_sn3.textEdited.connect(
            lambda: self.on_user_input_text(CONFIG_MENU_FIELD_TYPE.SN_TRI, self.ui.lineEdit_sn3))

        self.ui.lineEdit_project_name.textEdited.connect(
            lambda: self.on_user_input_text(CONFIG_MENU_FIELD_TYPE.PROJECT_NAME, self.ui.lineEdit_project_name))
        self.ui.lineEdit_lot.textEdited.connect(
            lambda: self.on_user_input_text(CONFIG_MENU_FIELD_TYPE.LOT_COUNT, self.ui.lineEdit_lot))

        # radioButton_sns2_2 = sn sn sn
        self.ui.radioButton_sns2_2.clicked.connect(
            lambda: self.on_user_change_radio_btn(SN_COUNT_TYPE.SN_TRIPLE))
        self.ui.radioButton_sns2.clicked.connect(
            lambda: self.on_user_change_radio_btn(SN_COUNT_TYPE.SN_DOUBLE))

        self.set_enable_all_menu(True)

    def get_main_window(self):
        return self.__main_window

    def set_default_all_fields(self):

        config_list = [
            CONFIG_MENU_FIELD_TYPE.SN_ONE,
            CONFIG_MENU_FIELD_TYPE.SN_TWO,
            CONFIG_MENU_FIELD_TYPE.SN_TRI,
            CONFIG_MENU_FIELD_TYPE.PROJECT_NAME,
            CONFIG_MENU_FIELD_TYPE.SNS_COUNT,
            CONFIG_MENU_FIELD_TYPE.LOT_COUNT
        ]
        for cid in config_list:
            self.set_default_fields(cid)

    def set_default_fields(self, config_id: CONFIG_MENU_FIELD_TYPE):
        if config_id == CONFIG_MENU_FIELD_TYPE.SNS_COUNT:
            self.ui.radioButton_sns2_2.click()
            self.rehide_sns3_changed_field()
        elif config_id == CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
            self.set_field_value(config_id, "My Project")
        elif config_id == CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
            self.set_field_value(config_id, 500)
        elif config_id == CONFIG_MENU_FIELD_TYPE.SN_ONE:
            self.set_field_value(config_id, "SN1")
        elif config_id == CONFIG_MENU_FIELD_TYPE.SN_TWO:
            self.set_field_value(config_id, "SN2")
        elif config_id == CONFIG_MENU_FIELD_TYPE.SN_TRI:
            self.set_field_value(config_id, "SN3")

    def rehide_sns3_changed_field(self):
        if self.ui.radioButton_sns2_2.isChecked():
            self.ui.lineEdit_sn3.setEnabled(True)
        elif self.ui.radioButton_sns2.isChecked():
            self.ui.lineEdit_sn3.setEnabled(False)

    def on_user_change_radio_btn(self, sn_count_type: SN_COUNT_TYPE):
        self.rehide_sns3_changed_field()

    def on_user_input_text(self, sn_type: CONFIG_MENU_FIELD_TYPE, text_field: UI_ConfigWindow):
        input_text: str = text_field.text()

        let_success = False
        if isinstance(input_text, str):
            if sn_type in (CONFIG_MENU_FIELD_TYPE.SN_ONE,
                           CONFIG_MENU_FIELD_TYPE.SN_TWO,
                           CONFIG_MENU_FIELD_TYPE.SN_TRI):
                if 0 < len(input_text) < 64:
                    let_success = True
                else:
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text="Ошибка во вводе!\n"
                                          f"Длинна текста от 1 до 64 символа!",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    self.set_default_fields(sn_type)

            elif sn_type == CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
                if 0 < len(input_text) < 64:
                    let_success = True
                else:
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text="Ошибка во вводе!\n"
                                          f"Длинна текста от 1 до 64 символа!",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    self.set_default_fields(sn_type)

            elif sn_type == CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
                let_success = False
                if input_text.isdigit():
                    count = int(input_text)
                    if 1 < count < MAX_LOT_COUNT:
                        let_success = True

                if not let_success:

                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text="Ошибка во вводе!\n"
                                          f"Количество лота может быть от 1 до {MAX_LOT_COUNT} штук!",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    self.set_default_fields(sn_type)

    def set_enable_all_menu(self, status: bool):
        self.ui.centralwidget.setEnabled(status)

    def get_field_value(self, config_type: CONFIG_MENU_FIELD_TYPE) -> any:
        """ Вернёт значение филда из переменной """
        match config_type:
            case CONFIG_MENU_FIELD_TYPE.SN_ONE:
                return self.ui.lineEdit_sn1.text()
            case CONFIG_MENU_FIELD_TYPE.SN_TWO:
                return self.ui.lineEdit_sn2.text()
            case CONFIG_MENU_FIELD_TYPE.SN_TRI:
                return self.ui.lineEdit_sn3.text()
            case CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
                return self.ui.lineEdit_project_name.text()
            case CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
                return self.ui.lineEdit_lot.text()
        return None

    def set_field_value(self, config_type: CONFIG_MENU_FIELD_TYPE, set_value: any) -> any:
        """ Задаст значение и переменной и филду! """
        match config_type:
            case CONFIG_MENU_FIELD_TYPE.SN_ONE:
                self.ui.lineEdit_sn1.setText(set_value)
            case CONFIG_MENU_FIELD_TYPE.SN_TWO:
                self.ui.lineEdit_sn2.setText(set_value)
            case CONFIG_MENU_FIELD_TYPE.SN_TRI:
                self.ui.lineEdit_sn3.setText(set_value)
            case CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
                self.ui.lineEdit_project_name.setText(set_value)
            case CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
                self.ui.lineEdit_lot.setText(str(set_value))


    def on_user_pressed_save_create(self):
        mw = self.get_main_window()
        if mw:
            if CProject.get_project_current_status() == PROJECT_TYPE.NONE_PROJECT:
                if mw.get_programm_status() == PROGRAM_STATUS.NO_PROJECT:
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.PROJECT_NAME,
                                             self.get_field_value(CONFIG_MENU_FIELD_TYPE.PROJECT_NAME))
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.SN_ONE,
                                             self.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_ONE))
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.SN_TWO,
                                             self.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_TWO))
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.SN_TRI,
                                             self.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_TRI))
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.LOT_COUNT,
                                             self.get_field_value(CONFIG_MENU_FIELD_TYPE.LOT_COUNT))

                    CProject.set_project_current_status(PROJECT_TYPE.NEW_PROJECT)
                    mw.carea_unit.delete_fields()

                    mw.switch_program_status(PROGRAM_STATUS.IN_JOB)



    def on_user_pressed_default(self):
        self.set_default_all_fields()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
