from connexion.database_sqlite import DatabaseSqlite
from entities.produit import Produit

class SqliteProduit:
    def __init__(self):
        self.conn = DatabaseSqlite.get_instance().get_connection()

    def cree_table(self):
        req = """
        CREATE TABLE IF NOT EXISTS produit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prix REAL
        )
        """
        cur = self.conn.cursor()
        cur.execute(req)
        self.conn.commit()

    def ajouter_produit(self, produit : Produit):
        req = "INSERT INTO produit(nom,prix) VALUES (?,?)"
        cur = self.conn.cursor()
        cur.execute(req,(produit.get_nom(),produit.get_prix()))
        self.conn.commit()
        return cur.lastrowid
    
    def trouver_produits(self):
        req = "SELECT * FROM produit"
        cur = self.conn.cursor()
        cur.execute(req)
        return cur.fetchall()
    
    def modifier_prix(self,produit:Produit):
        req = "UPDATE produit SET prix = ? WHERE id = ?"
        cur = self.conn.cursor()
        cur.execute(req,(produit.get_prix(),produit.get_id()))
        self.conn.commit()