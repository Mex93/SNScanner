import sqlite3


class CDatabase(sqlite3):

    def __new__(cls, *args, **kwargs):
        cls.connect_handle = None
        return cls

    @classmethod
    def connect_to_db(cls, db_name: str):
        if cls.connect_handle is None:
            return cls.connect_handle
        try:
            connection = sqlite3.connect(f'{db_name}.db')
            cls.connect_handle = connection
            return connection
        except:
            return None

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
