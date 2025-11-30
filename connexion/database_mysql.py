import mysql.connector
from mysql.connector import Error

class DatabaseMysql:

    _instance = None

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "boutique"
            )
        except Error as e:
            print("Connection echoue!")
            raise

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DatabaseMysql()
        return cls._instance
    
    def get_connection(self):
        return self.conn