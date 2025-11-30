from entities.produit import Produit
from entities.client import Client

from Mysql.mysql_dao_client import MysqlClient
from Mysql.mysql_dao_produit import MysqlProduit
from Sqlite.sqlite_dao_client import SqliteClient
from Sqlite.sqlite_dao_produit import SqliteProduit

def main():
    print("=== Mini-projet Boutique ===")
    print("Choisissez la base de données:")
    print("1. SQLite")
    print("2. MySQL")
    db_choice = input("Votre choix (1/2): ")

    if db_choice == "1":
        produit_dao = SqliteProduit()
        client_dao = SqliteClient()
        # Create tables if not exist
        produit_dao.cree_table()
        client_dao.cree_table()
    elif db_choice == "2":
        produit_dao = MysqlProduit()
        client_dao = MysqlClient()
    else:
        print("Choix invalide!")
        return

    while True:
        print("\n=== Menu ===")
        print("1. Ajouter un produit")
        print("2. Lister tous les produits")
        print("3. Modifier le prix d'un produit")
        print("4. Ajouter un client")
        print("5. Lister tous les clients")
        print("6. Rechercher un client par email")
        print("0. Quitter")

        choice = input("Votre choix: ")

        if choice == "1":
            nom = input("Nom du produit: ")
            prix = float(input("Prix: "))
            p = Produit(None, nom, prix)
            pid = produit_dao.ajouter_produit(p)
            print(f"Produit ajouté avec id={pid}")
        
        elif choice == "2":
            produits = produit_dao.trouver_produits()
            for p in produits:
                print(f"ID: {p['id']}, Nom: {p['nom']}, Prix: {p['prix']}")
        
        elif choice == "3":
            pid = int(input("ID du produit: "))
            nouveau_prix = float(input("Nouveau prix: "))
            p = Produit(pid, "", nouveau_prix)
            produit_dao.modifier_prix(p)
            print("Prix modifié avec succès!")

        elif choice == "4":
            nom = input("Nom du client: ")
            email = input("Email: ")
            c = Client(None, nom, email)
            cid = client_dao.ajouter_client(c)
            print(f"Client ajouté avec id={cid}")

        elif choice == "5":
            clients = client_dao.trouver_clients()
            for c in clients:
                print(f"ID: {c['id']}, Nom: {c['nom']}, Email: {c['email']}")

        elif choice == "6":
            email = input("Email à rechercher: ").strip()
            client = client_dao.touver_client_par_email(email)
            if client:
                print(f"ID: {client['id']}, Nom: {client['nom']}, Email: {client['email']}")
            else:
                print("Client introuvable!")

        elif choice == "0":
            print("Au revoir!")
            break
        else:
            print("Choix invalide!")

if __name__ == "__main__":
    main()
