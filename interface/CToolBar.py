import sys

from PySide6.QtWidgets import QMainWindow

from ui.untitled import Ui_MainWindow



class CToolBar():
    main_window = None
    config_window = None

    def __init__(self, main_ui: Ui_MainWindow):
        self.__set_main_window(main_ui)

    @classmethod
    def __set_main_window(cls, main_ui: Ui_MainWindow):
        cls.main_window = main_ui

