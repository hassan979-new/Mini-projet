
# 🧮 Mini-projet

## 📘 Description

Ce mini-projet illustre la conception d’une application console de gestion de boutique en Python :

- Connexion aux bases de données MySQL et SQLite via Singleton

- Définition des entités métier : Client et Produit

- Implémentation des DAO (Data Access Object) pour encapsuler les opérations CRUD

- Interface console interactive permettant d’ajouter, lister, modifier et rechercher

## 📂 Project Structure
````
projets/
├── connexion/
│   ├── database_mysql.py
│   └── database_sqlite.py
├── entities/
│   ├── client.py
│   └── produit.py
├── db/
│   ├── boutique.db
│   └── boutique.sql
├── Mysql/
│   ├── mysql_dao_client.py
│   └── mysql_dao_produit.py
├── Sqlite/
│   ├── sqlite_dao_client.py
│   └── sqlite_dao_produit.py
├── app/
│   └── main.py
└── README.md
````


## ⚙️ Features

### **1.** Connexion aux bases de données
Classe DatabaseMysql

- Attributs : conn (connexion MySQL)

Méthodes :

- __init__() : établit la connexion à la base MySQL boutique

- get_instance() : Singleton, retourne l’instance unique

- get_connection() : fournit la connexion active

Classe DatabaseSqlite

- Attributs : conn (connexion SQLite)

Méthodes :

- __init__() : crée/ouvre la base SQLite boutique.db

- get_instance() : Singleton, retourne l’instance unique

- get_connection() : fournit la connexion active

### **2.** Entités métier
Classe Client

- Attributs privés : __id, __nom, __email

Méthodes :

- get_id(), get_nom(), get_email() : accès aux attributs

- __str__() : représentation textuelle

Classe Produit

- Attributs privés : __id, __nom, __prix

Méthodes :

- id (property) : accès direct à l’identifiant

- get_id(), get_nom(), get_prix() : accès aux attributs

- __str__() : représentation textuelle

### **3.** DAO MySQL
Classe MysqlClient

Méthodes :

- ajouter_client(client) : insertion d’un client

- trouver_clients() : récupération de tous les clients

- touver_client_par_email(email) : recherche par email

Classe MysqlProduit

- Méthodes :

- ajouter_produit(produit) : insertion d’un produit

- trouver_produits() : récupération de tous les produits

- modifier_prix(produit) : mise à jour du prix

### **4.** DAO SQLite
Classe SqliteClient

Méthodes :

- cree_table() : création de la table client si absente

- ajouter_client(client) : insertion d’un client

- trouver_clients() : récupération de tous les clients

- touver_client_par_email(email) : recherche par email

Classe SqliteProduit

Méthodes :

- cree_table() : création de la table produit si absente

- ajouter_produit(produit) : insertion d’un produit

- trouver_produits() : récupération de tous les produits

- modifier_prix(produit) : mise à jour du prix

### **5.** Interface console – main.py
- Choix du SGBD : SQLite ou MySQL

Menu interactif :

- Ajouter un produit

- Lister tous les produits

- Modifier le prix d’un produit

- Ajouter un client

- Lister tous les clients

- Rechercher un client par email

- Quitter
## 🖥️ Example Execution
##### video de demonstration SQLite:
[Watch on Google Drive](https://drive.google.com/file/d/1Guowp7N8lRZlcr80iy7J6c2KJIbmPeF1/view?usp=sharing)
##### video de demonstration MySQL:
[Watch on Google Drive](https://drive.google.com/file/d/1BUSb3BJDd8YGcDFYAz1BZlaXveTC4svB/view?usp=sharing)
- <img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/f9a41e60-7ab3-47b9-9960-eba782287ff2" />
- <img width="960" height="504" alt="image" src="https://github.com/user-attachments/assets/673d3d0b-9265-4151-acf9-01405e741c5a" />
## 💡 Concepts Practiced

- Utilisation du pattern Singleton pour gérer les connexions aux bases de données

- Encapsulation des entités métier avec attributs privés et méthodes d’accès

- Implémentation du pattern DAO pour séparer la logique métier de l’accès aux données

- Compatibilité multi-SGBD (MySQL et SQLite) avec une interface commune

- Développement d’une interface console simple et efficace pour tester les fonctionnalités
## 🧑‍💻 Author

- 👤 Agouram Hassan
- 🏫 Programmation orientée objet : python
- 🎓 Instructor	Mr.LACHGAR
- 📅 30	novembre 2025
