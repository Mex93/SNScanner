from enums import SMBOX_ICON_TYPE, SN_COUNT_TYPE, PROJECT_TYPE, PROGRAM_STATUS, CONFIG_MENU_FIELD_TYPE
from ui.untitled import Ui_MainWindow
from common import MAX_LOT_COUNT

class CProject:
    __project_current_status: PROJECT_TYPE = PROJECT_TYPE.NONE_PROJECT
    lot_count = 0
    sn_1_name = None
    sn_2_name = None
    sn_3_name = None
    sn_type_changed = None
    __current_project_name = None
    __sql_project_config_id = 0
    __sql_project_data_table_id = 0

    @classmethod
    def set_default(cls):
        project_name = cls.get_default_fields(CONFIG_MENU_FIELD_TYPE.PROJECT_NAME)
        sn1 = cls.get_default_fields(CONFIG_MENU_FIELD_TYPE.SN_ONE)
        sn2 = cls.get_default_fields(CONFIG_MENU_FIELD_TYPE.SN_TWO)
        sn3 = cls.get_default_fields(CONFIG_MENU_FIELD_TYPE.SN_TRI)
        sns_count = cls.get_default_fields(CONFIG_MENU_FIELD_TYPE.SNS_COUNT)
        lot_count = cls.get_default_fields(CONFIG_MENU_FIELD_TYPE.LOT_COUNT)
        #
        cls.set_field_value(CONFIG_MENU_FIELD_TYPE.PROJECT_NAME, project_name)
        cls.set_field_value(CONFIG_MENU_FIELD_TYPE.SN_ONE, sn1)
        cls.set_field_value(CONFIG_MENU_FIELD_TYPE.SN_TWO, sn2)
        cls.set_field_value(CONFIG_MENU_FIELD_TYPE.SN_TRI, sn3)
        cls.set_field_value(CONFIG_MENU_FIELD_TYPE.SNS_COUNT, sns_count)
        cls.set_field_value(CONFIG_MENU_FIELD_TYPE.LOT_COUNT, lot_count)

    @classmethod
    def get_default_fields(cls, config_id: CONFIG_MENU_FIELD_TYPE):
        if config_id == CONFIG_MENU_FIELD_TYPE.SNS_COUNT:
            return SN_COUNT_TYPE.SN_DOUBLE
        elif config_id == CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
            return 'My Project'
        elif config_id == CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
            return 500
        elif config_id == CONFIG_MENU_FIELD_TYPE.SN_ONE:
            return 'SN1'
        elif config_id == CONFIG_MENU_FIELD_TYPE.SN_TWO:
            return 'SN2'
        elif config_id == CONFIG_MENU_FIELD_TYPE.SN_TRI:
            return 'SN3'
        elif config_id == CONFIG_MENU_FIELD_TYPE.MAX_LOT_COUNT:
            return MAX_LOT_COUNT


    @classmethod
    def set_sql_config_id(cls, cid: int):
        if isinstance(cid, int):
            cls.__sql_project_config_id = cid
        else:
            raise TypeError("SQL Config ID is not integer!")

    @classmethod
    def set_sql_data_id(cls, cid: int):
        if isinstance(cid, int):
            cls.__sql_project_data_table_id = cid
        else:
            raise TypeError("SQL Data Table ID is not integer!")

    @classmethod
    def get_data_sql_table_name(cls) -> str:
        if cls.__sql_project_data_table_id:
            return f"project_data_{cls.__sql_project_data_table_id}"
        else:
            raise ValueError("SQL Table Name is Null")

    @classmethod
    def get_config_sql_id(cls) -> int:
        if cls.__sql_project_config_id:
            return cls.__sql_project_config_id
        else:
            raise ValueError("SQL Config ID is Null")

    ####
    @classmethod
    def get_project_current_status(cls) -> PROJECT_TYPE:
        return cls.__project_current_status

    @classmethod
    def set_project_current_status(cls, status: PROJECT_TYPE):
        cls.__project_current_status = status

    @classmethod
    def set_programm_current_status(cls, status: PROGRAM_STATUS):
        cls.__program_current_status = status

    @classmethod
    def set_field_value(cls, field_type: CONFIG_MENU_FIELD_TYPE, set_value: any) -> any:
        """ Задаст значение и переменной и филду! """
        match field_type:
            case CONFIG_MENU_FIELD_TYPE.SN_ONE:
                cls.sn_1_name = set_value
            case CONFIG_MENU_FIELD_TYPE.SN_TWO:
                cls.sn_2_name = set_value
            case CONFIG_MENU_FIELD_TYPE.SN_TRI:
                cls.sn_3_name = set_value
            case CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
                cls.__current_project_name = set_value
            case CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
                cls.lot_count = set_value
            case CONFIG_MENU_FIELD_TYPE.SNS_COUNT:
                cls.sn_type_changed = set_value

    @classmethod
    def get_field_value(cls, field_type: CONFIG_MENU_FIELD_TYPE) -> str | int | SN_COUNT_TYPE:
        """ Задаст значение и переменной и филду! """
        match field_type:
            case CONFIG_MENU_FIELD_TYPE.SN_ONE:
                return cls.sn_1_name
            case CONFIG_MENU_FIELD_TYPE.SN_TWO:
                return cls.sn_2_name
            case CONFIG_MENU_FIELD_TYPE.SN_TRI:
                return cls.sn_3_name
            case CONFIG_MENU_FIELD_TYPE.PROJECT_NAME:
                return cls.__current_project_name
            case CONFIG_MENU_FIELD_TYPE.LOT_COUNT:
                return int(cls.lot_count)
            case CONFIG_MENU_FIELD_TYPE.SNS_COUNT:
                return cls.sn_type_changed

    ###
    @classmethod
    def set_project_name(cls, name: str) -> bool:
        if name:
            cls.__current_project_name = name
            return True
        else:
            raise ValueError("No name for project")
