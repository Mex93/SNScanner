from enums import SMBOX_ICON_TYPE, SN_COUNT_TYPE, PROJECT_TYPE, PROGRAM_STATUS


class CProject:
    def __init__(self):
        self.__program_current_status: PROGRAM_STATUS = PROGRAM_STATUS.NO_PROJECT
        self.__project_current_status: PROJECT_TYPE = PROJECT_TYPE.NONE_PROJECT
        self.__current_project_name = None
        self.__sql_project_config_id = 0
        self.__sql_project_data_table_id = 0

    def set_sql_config_id(self, cid: int):
        if isinstance(cid, int):
            self.__sql_project_config_id = cid
        else:
            raise TypeError("SQL Config ID is not integer!")

    def set_sql_data_id(self, cid: int):
        if isinstance(cid, int):
            self.__sql_project_data_table_id = cid
        else:
            raise TypeError("SQL Data Table ID is not integer!")

    def get_data_sql_table_name(self) -> str:
        if self.__sql_project_data_table_id:
            return f"project_data_{self.__sql_project_data_table_id}"
        else:
            raise ValueError("SQL Table Name is Null")

    def get_config_sql_id(self) -> int:
        if self.__sql_project_config_id:
            return self.__sql_project_config_id
        else:
            raise ValueError("SQL Config ID is Null")

    ####
    def get_project_current_status(self) -> PROJECT_TYPE:
        return self.__project_current_status

    def set_project_current_status(self, status: PROJECT_TYPE):
        self.__project_current_status = status

    ####
    def get_programm_current_status(self) -> PROGRAM_STATUS:
        return self.__program_current_status

    def set_programm_current_status(self, status: PROGRAM_STATUS):
        self.__program_current_status = status

    ###
    def set_project_name(self, name: str) -> bool:
        if name:
            self.__current_project_name = name
            return True
        else:
            raise ValueError("No name for project")

    def get_project_name(self) -> str:
        return self.__current_project_name
