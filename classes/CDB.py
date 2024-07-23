import sqlite3
import os

from classes.CProject import CProject, CONFIG_MENU_FIELD_TYPE


class CDBTablesName:
    fd_project_data_ = 'project_data_'
    fd_project_settings = 'project_settings'


class CDBTableProjectFields:
    fd_project_name = 'project_name'
    fd_project_pk = 'project_pk'
    fd_lot_count = 'lot_count'
    fd_sn_count = 'sn_count'
    fd_sn_1_name = 'sn_1_name'
    fd_sn_2_name = 'sn_2_name'
    fd_sn_3_name = 'sn_3_name'


class CDBTableFields:
    fd_sn_1 = 'sn_1'
    fd_sn_2 = 'sn_2'
    fd_sn_3 = 'sn_3'
    fd_scan_date = 'scan_date'
    fd_table_index = 'table_index'
    fd_pr_key = 'fields_pk'


class CDatabase:
    standart_main_folder_name = 'databases'
    cancelled_folder_name = 'databases_cancelled'

    def __init__(self):
        self.connect_handle: sqlite3 = None

    @classmethod
    def get_db_name(cls) -> str:
        return 'projects_data'

    def connect_to_db(self, db_name: str):
        if self.connect_handle is not None:
            return self.connect_handle

        try:
            folder_its_ok = False
            if self.is_folder_already(self.standart_main_folder_name):
                folder_its_ok = True
            else:
                if self.create_folder(self.standart_main_folder_name):
                    folder_its_ok = True

            if folder_its_ok:
                file_patch = self.get_file_patch(self.standart_main_folder_name, db_name)
                connection = sqlite3.connect(file_patch)
                self.connect_handle = connection
                return connection
        except:
            return None

    @classmethod
    def is_folder_already(cls, folder_name: str) -> bool:
        return os.path.isdir(f"{folder_name}")

    @classmethod
    def get_file_patch(cls, folder_name: str, file_name: str) -> str:
        return f"{folder_name}/{file_name}.db"

    @classmethod
    def create_folder(cls, folder_name: str) -> bool:
        try:
            os.mkdir(folder_name + "/")
            return cls.is_folder_already(folder_name)
        except:
            return False

    def get_handle(self):
        return self.connect_handle

    def disconnect(self):
        if self.connect_handle is None:
            return False

        self.connect_handle.close()
        self.connect_handle = None
        return True

    def is_dbfile_exist(self, db_name: str):
        pass

    def create_project_settings_table(self, transaction=False) -> bool:

        handle = self.get_handle()
        if handle:
            query = (f'CREATE TABLE IF NOT EXISTS {CDBTablesName.fd_project_settings} ('
                     f'{CDBTableProjectFields.fd_project_name} TEXT DEFAULT "Main project",'
                     f'{CDBTableProjectFields.fd_project_pk} INTEGER UNIQUE,'
                     f'{CDBTableProjectFields.fd_lot_count} INTEGER DEFAULT 10000,'
                     f'{CDBTableProjectFields.fd_sn_count} INTEGER DEFAULT 2,'
                     f'{CDBTableProjectFields.fd_sn_1_name} TEXT DEFAULT "SN1",'
                     f'{CDBTableProjectFields.fd_sn_2_name} TEXT DEFAULT "SN2",'
                     f'{CDBTableProjectFields.fd_sn_3_name} TEXT DEFAULT "SN3",'
                     f'PRIMARY KEY({CDBTableProjectFields.fd_project_pk} AUTOINCREMENT)'
                     f')')

            cursor = handle.cursor()
            cursor.execute(query)
            if not transaction:
                handle.commit()
            return True

    def insert_new_project(self, transaction=False) -> bool | int:

        handle: sqlite3 = self.get_handle()
        if handle:
            pr_name = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.PROJECT_NAME)
            sn1 = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_ONE)
            sn2 = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_TWO)
            sn3 = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.SN_TRI)
            lot_count = CProject.get_field_value(CONFIG_MENU_FIELD_TYPE.LOT_COUNT)
            sns_count = int(CProject.get_default_fields(CONFIG_MENU_FIELD_TYPE.SNS_COUNT))

            query = (f'INSERT INTO {CDBTablesName.fd_project_settings} ('
                     f'{CDBTableProjectFields.fd_project_name},'
                     f'{CDBTableProjectFields.fd_lot_count}, '
                     f'{CDBTableProjectFields.fd_sn_count},'
                     f'{CDBTableProjectFields.fd_sn_1_name}, '
                     f'{CDBTableProjectFields.fd_sn_2_name},'
                     f'{CDBTableProjectFields.fd_sn_3_name}'
                     ') '
                     'VALUES '
                     '(?, ?, ?, ?, ?, ?);')

            cursor = handle.cursor()
            cursor.execute(query, (pr_name, lot_count, sns_count, sn1, sn2, sn3))

            last_id = cursor.lastrowid
            if not transaction:
                handle.commit()
            return last_id
        return False

    def create_project_fields_table(self, project_index: int, transaction=False) -> bool | int:

        handle = self.get_handle()
        if handle:
            query = (f'CREATE TABLE IF NOT EXISTS {CDBTablesName.fd_project_data_}{project_index} ('
                     f'{CDBTableFields.fd_sn_1}	TEXT DEFAULT NULL,'
                     f'{CDBTableFields.fd_sn_2}	TEXT DEFAULT NULL,'
                     f'{CDBTableFields.fd_sn_3}	TEXT DEFAULT NULL,'
                     f'{CDBTableFields.fd_scan_date} INTEGER DEFAULT 0,'
                     f'{CDBTableFields.fd_table_index}	INTEGER DEFAULT 0,'
                     f'{CDBTableFields.fd_pr_key}	INTEGER NOT NULL,'
                     f'PRIMARY KEY({CDBTableFields.fd_pr_key} AUTOINCREMENT)'
                     f')')

            cursor = handle.cursor()
            cursor.execute(query)
            if not transaction:
                handle.commit()
            return True

    def set_transaction_begin(self):
        handle = self.get_handle()
        if handle:
            cursor = handle.cursor()
            cursor.execute('BEGIN')
            return True

    def set_transaction_rollback(self):
        handle = self.get_handle()
        if handle:
            cursor = handle.cursor()
            cursor.execute('ROLLBACK')
            return True

    def set_transaction_commit(self):
        handle = self.get_handle()
        if handle:
            cursor = handle.cursor()
            cursor.execute('COMMIT')
            return True

