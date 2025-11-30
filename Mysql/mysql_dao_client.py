from connexion.database_mysql import DatabaseMysql
from entities.client import Client

class MysqlClient:
    def __init__(self):
        self.conn = DatabaseMysql.get_instance().get_connection()

    def ajouter_client(self, client : Client):
        req = "INSERT INTO client(nom,email) VALUES (%s,%s)"
        curs = self.conn.cursor()
        curs.execute(req,(client.get_nom(),client.get_email()))
        self.conn.commit()
        return curs.lastrowid
    
    def trouver_clients(self):
        req = "SELECT * FROM client"
        curs = self.conn.cursor(dictionary=True)
        curs.execute(req)
        resultat = curs.fetchall()
        return resultat
    
    def touver_client_par_email(self,email):
        req = "SELECT * FROM client WHERE email = %s"
        cur = self.conn.cursor(dictionary=True)
        cur.execute(req,(email,))
        return cur.fetchone()
