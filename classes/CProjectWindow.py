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
from classes.CInputArea import CInputArea, CInputUnit
from common import MAX_LOT_COUNT, MIN_LOT_COUNT, MAX_FIELDS_ON_PAGE


class CProjectWindow(QMainWindow):
    def __init__(self, window_type: WINDOW_TYPE, main_window, parent=None):
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
        var = CProject.get_default_fields(config_id)
        self.set_field_value(config_id, var)

    def rehide_sns3_changed_field(self):

        types = self.get_field_value(CONFIG_MENU_FIELD_TYPE.SNS_COUNT)
        if types == SN_COUNT_TYPE.SN_TRIPLE:
            self.ui.lineEdit_sn3.setEnabled(True)
        if types == SN_COUNT_TYPE.SN_DOUBLE:
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
                    if MIN_LOT_COUNT < count < MAX_LOT_COUNT:
                        let_success = True

                if not let_success:
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text="Ошибка во вводе!\n"
                                          f"Количество лота может быть от {MIN_LOT_COUNT} до {MAX_LOT_COUNT} штук!",
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
            case CONFIG_MENU_FIELD_TYPE.SNS_COUNT:
                if self.ui.radioButton_sns2_2.isChecked():
                    return SN_COUNT_TYPE.SN_TRIPLE
                elif self.ui.radioButton_sns2.isChecked():
                    return SN_COUNT_TYPE.SN_DOUBLE
                else:
                    return SN_COUNT_TYPE.SN_NONE
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
            case CONFIG_MENU_FIELD_TYPE.SNS_COUNT:
                set_value: SN_COUNT_TYPE
                if set_value == SN_COUNT_TYPE.SN_TRIPLE:
                    self.ui.radioButton_sns2_2.click()
                elif set_value == SN_COUNT_TYPE.SN_DOUBLE:
                    self.ui.radioButton_sns2.click()
                self.rehide_sns3_changed_field()

    def on_user_pressed_save_create(self):
        mw = self.get_main_window()
        if mw:
            if CProject.get_project_current_status() == PROJECT_TYPE.NONE_PROJECT:
                if mw.get_programm_status() == PROGRAM_STATUS.NO_PROJECT:

                    project_name = self.get_field_value(CONFIG_MENU_FIELD_TYPE.PROJECT_NAME)
                    sn1 = self.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_ONE)
                    sn2 = self.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_TWO)
                    sn3 = self.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_TRI)
                    lot_count = self.get_field_value(CONFIG_MENU_FIELD_TYPE.LOT_COUNT)
                    sns_type = self.get_field_value(CONFIG_MENU_FIELD_TYPE.SNS_COUNT)

                    if '' in (project_name, sn1, sn2, sn3, lot_count):
                        logging.warning("Ошибка! Филды пустые")
                        return

                    if sns_type == SN_COUNT_TYPE.SN_NONE:
                        logging.warning("Ошибка! Чекбокс SNS не выбран")
                        return

                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.PROJECT_NAME, project_name)
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.SN_ONE, sn1)
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.SN_TWO, sn2)
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.SN_TRI, sn3)
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.LOT_COUNT, lot_count)
                    CProject.set_field_value(CONFIG_MENU_FIELD_TYPE.SNS_COUNT, sns_type)

                    CProject.set_project_current_status(PROJECT_TYPE.NEW_PROJECT)
                    CInputArea.set_name_for_labels()

                    CInputArea.set_start()
                    mw.switch_program_status(PROGRAM_STATUS.IN_JOB)

                    db_unit = CDatabase()
                    try:

                        handler: CDatabase = db_unit.connect_to_db(CDatabase.get_db_name())
                        if handler:
                            db_unit.create_project_settings_table()
                            row_id = db_unit.insert_new_project()
                            if row_id:
                                db_unit.create_project_fields_table(row_id)

                    except Exception as err:
                        logging.critical(f"Ошибка!!! {err}", )
                        print(f"Ошибка!!! {err}", )
                    finally:
                        db_unit.disconnect()

                    self.hide()

    def on_user_pressed_default(self):
        self.set_default_all_fields()
