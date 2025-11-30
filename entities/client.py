class Client:
    def __init__(self, id:int, nom:str, email:str):
        self.__id = id
        self.__nom = nom
        self.__email = email

    def get_id(self):
        return self.__id
    
    def get_nom(self):
        return self.__nom
    
    def get_email(self):
        return self.__email

    def __str__(self):
        return f"Client: [{self.__id}, {self.__nom}, {self.__email}]"