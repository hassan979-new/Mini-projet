from connexion.database_mysql import DatabaseMysql
from entities.produit import Produit

class MysqlProduit:
    def __init__(self):
        self.conn = DatabaseMysql.get_instance().get_connection()

    def ajouter_produit(self, produit:Produit):
        req = "INSERT INTO produit (nom,prix) VALUES (%s,%s)"
        curs = self.conn.cursor()
        curs.execute(req,(produit.get_nom(),produit.get_prix()))
        self.conn.commit()
        return curs.lastrowid
    
    def trouver_produits(self):
        req = "SELECT * FROM produit"
        curs = self.conn.cursor(dictionary=True)
        curs.execute(req)
        resultat = curs.fetchall()
        return resultat
    
    def modifier_prix(self, produit : Produit):
        req = "UPDATE produit SET prix = %s WHERE id = %s"
        curs = self.conn.cursor()
        curs.execute(req,(produit.get_prix(),produit.get_id()))
        self.conn.commit()