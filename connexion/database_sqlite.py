import sqlite3

class DatabaseSqlite:
    _instance = None

    def __init__(self):
        self.conn = sqlite3.connect("db/boutique.db")
        self.conn.row_factory = sqlite3.Row

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DatabaseSqlite()
        return cls._instance
    
    def get_connection(self):
        return self.conn
    
    