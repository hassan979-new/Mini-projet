class Produit:
    def __init__(self, id:int, nom:str, prix:float):
        self.__id = id
        self.__nom = nom
        self.__prix = prix

    @property
    def id(self):
        return self.__id

    def get_id(self):
        return self.__id
    
    def get_nom(self):
        return self.__nom
    
    def get_prix(self):
        return self.__prix

    def __str__(self):
        return f"Produit:[{self.__id}, {self.__nom}, {self.__prix}]"