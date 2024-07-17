import sqlite3
import os


class CDatabase:
    standart_main_folder_name = 'databases'
    cancelled_folder_name = 'databases_cancelled'
    connect_handle = None
    def __new__(cls, *args, **kwargs):
        cls.connect_handle = None
        return cls

    @classmethod
    def connect_to_db(cls, db_name: str):
        if cls.connect_handle is not None:
            return cls.connect_handle
        try:
            folder_its_ok = False
            if cls.is_folder_already(cls.standart_main_folder_name):
                folder_its_ok = True
            else:
                if cls.create_folder(cls.standart_main_folder_name):
                    folder_its_ok = True

            if folder_its_ok:
                file_patch = cls.get_file_patch(cls.standart_main_folder_name, db_name)
                connection = sqlite3.connect(file_patch)
                cls.connect_handle = connection
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

    @classmethod
    def get_handle(cls):
        return cls.connect_handle

    @classmethod
    def disconnect(cls):
        if cls.connect_handle is None:
            return False

        cls.connect_handle.close()
        cls.connect_handle = None
        return True

    def is_dbfile_exist(self, db_name: str):
        pass
