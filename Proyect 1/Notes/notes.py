from BdConection.conect import ConectDatabase
from datetime import datetime

class Notes:

    def __init__(self,host = None,user = None,password_database = None,database = None):
        self.conection = ConectDatabase(
            host,
            user,
            password_database,
            database,
        )
    def load_note (self,id_user,title,description):

        time = str(datetime.now())
        self.conection.insert_note(
            [id_user,title,description,time]
        )
        

    def view_note(self,id_user):
        consult = self.conection.consult_notes(
            [id_user]
        )

        if consult == None:
            print("No tienes ninguna nota")
        else:
            return consult

    def delete_note(self,id_user):
        list_delete = self.view_note(id_user)
        
        print("tienes las siguientes notas, cual quieres eliminar?")
        for i in list_delete:
            print(i[2])
        title_delete = str(input("ingresa el titulo de la nota a eliminar:"))

        self.conection.delete_notes(
            [id_user,title_delete]
        )
    
