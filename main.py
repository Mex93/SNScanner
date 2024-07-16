import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QFontDatabase

import PySide6.QtCore as qc


from ui.untitled import Ui_MainWindow
from ui.config_project_menu import Ui_MainWindow as UI_ConfigWindow

from interface.enums import CONFIG_MENU_FIELD_TYPE
from common import send_message_box
from enums import SMBOX_ICON_TYPE, SN_COUNT_TYPE, PROJECT_TYPE, PROGRAM_STATUS
from database.CDB import CDatabase
from project.CProject import CProject

# pyside6-uic .\ui\untitled.ui -o .\ui\untitled.py
# pyside6-rcc .\ui\res.qrc -o .\ui\res_rc.py
# Press the green button in the gutter to run the script.

MAX_LOT_COUNT = 10_000


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__base_program_version = "0.1"  # Менять при каждом обновлении любой из подпрограмм

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        self.setWindowTitle(f'SN Scan Квант 2024 v0.1')

        self.config_window = CConfigWindow()
        self.db_unit = CDatabase()
        self.cproject = CProject()

        # connects
        # self.ui.pb_code.clicked.connect(self.on_user_clicked_convert_button)
        # self.ui.pb_decode.clicked.connect(self.on_user_clicked_deconvert_button)

        self.ui.action_new_project.triggered.connect(self.on_user_clicked_new_project)
        self.ui.action_open.triggered.connect(self.on_user_focus)

    def on_user_clicked_new_project(self):
        self.set_config_menu(True)

    def on_user_focus(self):
        handler: CDatabase = self.db_unit.connect_to_db("my_test")
        if handler:
            print(handler)
            self.db_unit.disconnect()

    def set_config_menu(self, status: bool):
        if status:
            self.config_window.show()
            self.config_window.setFocus()
        else:
            self.config_window.hide()


    def set_program_to_default_state(self):
        self.


class CConfigWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = UI_ConfigWindow()
        self.ui.setupUi(self)
        QFontDatabase.addApplicationFont("designs/Iosevka Bold.ttf")
        self.setWindowTitle(f'Настройки проекта')

        self.project_name = None
        self.lot_count = 0
        self.sn_1_name = None
        self.sn_2_name = None
        self.sn_3_name = None
        self.sn_type_changed = None
        self.setWindowModality(qc.Qt.WindowModality.ApplicationModal)

        # connects
        # self.ui.pb_code.clicked.connect(self.on_user_clicked_convert_button)
        # self.ui.pb_decode.clicked.connect(self.on_user_clicked_deconvert_button)

        self.ui.pushButton_save.clicked.connect(self.on_user_pressed_save)
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

    def on_user_change_radio_btn(self, sn_count_type: SN_COUNT_TYPE):
        print(sn_count_type)



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
                    text_field.clear()

            elif sn_type == CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
                if 0 < len(input_text) < 64:
                    let_success = True
                else:
                    send_message_box(icon_style=SMBOX_ICON_TYPE.ICON_WARNING,
                                     text="Ошибка во вводе!\n"
                                          f"Длинна текста от 1 до 64 символа!",
                                     title="Внимание!",
                                     variant_yes="Закрыть", variant_no="", callback=None)
                    text_field.clear()

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
                    text_field.clear()

            if let_success:
                match sn_type:
                    case CONFIG_MENU_FIELD_TYPE.SN_ONE:
                        self.sn_1_name = input_text
                    case CONFIG_MENU_FIELD_TYPE.SN_TWO:
                        self.sn_2_name = input_text
                    case CONFIG_MENU_FIELD_TYPE.SN_TRI:
                        self.sn_3_name = input_text
                    case CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
                        self.project_name = input_text
                    case CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
                        self.lot_count = int(input_text)

    def set_enable_all_menu(self, status: bool):
        if status:
            self.load_placeholder()

        self.ui.centralwidget.setEnabled(status)

    def load_placeholder(self):
        # Что бы подстраховаться. Вдруг в филде будет что-то не то (((
        # Берём из переменной

        if self.sn_1_name:
            self.ui.lineEdit_sn1.setText(self.sn_1_name)
        else:
            self.ui.lineEdit_sn1.setText('')

        if self.sn_2_name:
            self.ui.lineEdit_sn2.setText(self.sn_2_name)
        else:
            self.ui.lineEdit_sn2.setText('')

        if self.sn_3_name:
            self.ui.lineEdit_sn3.setText(self.sn_3_name)
        else:
            self.ui.lineEdit_sn3.setText('')

        if self.project_name:
            self.ui.lineEdit_project_name.setText(self.project_name)
        else:
            self.ui.lineEdit_project_name.setText('')

        if self.lot_count:
            self.ui.lineEdit_lot.setText(self.project_name)
        else:
            self.ui.lineEdit_lot.setText('')

    def get_field_value(self, field_type: CONFIG_MENU_FIELD_TYPE) -> any:
        """ Вернёт значение филда из переменной """
        match field_type:
            case CONFIG_MENU_FIELD_TYPE.SN_ONE:
                return self.sn_1_name
            case CONFIG_MENU_FIELD_TYPE.SN_TWO:
                return self.sn_2_name
            case CONFIG_MENU_FIELD_TYPE.SN_TRI:
                return self.sn_3_name
            case CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
                return self.project_name
            case CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
                return self.lot_count
        return None

    def set_field_value(self, field_type: CONFIG_MENU_FIELD_TYPE, set_value: any) -> any:
        """ Задаст значение и переменной и филду! """
        match field_type:
            case CONFIG_MENU_FIELD_TYPE.SN_ONE:
                self.sn_1_name = set_value
                self.ui.lineEdit_sn1.setText(set_value)
            case CONFIG_MENU_FIELD_TYPE.SN_TWO:
                self.sn_2_name = set_value
                self.ui.lineEdit_sn2.setText(set_value)
            case CONFIG_MENU_FIELD_TYPE.SN_TRI:
                self.sn_3_name = set_value
                self.ui.lineEdit_sn3.setText(set_value)
            case CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
                self.project_name = set_value
                self.ui.lineEdit_project_name.setText(set_value)
            case CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
                self.lot_count = set_value
                self.ui.lineEdit_lot.setText(set_value)

    def on_user_pressed_save(self):
        print(1)

    def on_user_pressed_default(self):
        print(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
