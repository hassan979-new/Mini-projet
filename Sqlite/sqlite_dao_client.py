from connexion.database_sqlite import DatabaseSqlite
from entities.client import Client

class SqliteClient:
    def __init__(self):
        self.conn = DatabaseSqlite.get_instance().get_connection()

    def cree_table(self):
        req = """
        CREATE TABLE IF NOT EXISTS client (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            email TEXT
        )
        """
        cur = self.conn.cursor()
        cur.execute(req)
        self.conn.commit()

    def ajouter_client(self, client : Client):
        req = "INSERT INTO client(nom,email) VALUES (?,?)"
        cur = self.conn.cursor()
        cur.execute(req,(client.get_nom(),client.get_email()))
        self.conn.commit()
        return cur.lastrowid
    
    def trouver_clients(self):
        req = "SELECT * FROM client"
        cur = self.conn.cursor()
        cur.execute(req)
        return cur.fetchall()
    
    def touver_client_par_email(self,email):
        req = "SELECT * FROM client WHERE email = ?"
        cur = self.conn.cursor()
        cur.execute(req,(email,))
        return cur.fetchone()

    

