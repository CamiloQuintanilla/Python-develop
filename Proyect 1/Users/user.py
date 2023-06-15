from BdConection.conect import ConectDatabase
from datetime import date,datetime
import hashlib

class User:
    
    def __init__(self,name = None,last_name = None, email = None,password = None , host = None,user = None,password_database = None,database = None):
        self.name=name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.conection = ConectDatabase(
            host,
            user,
            password_database,
            database,
        )
    def user_register(self):

        time = str(date.today())
        secret_password = hashlib.sha256()
        secret_password.update(self.password.encode('utf8'))

        self.conection.insert_user(
            [self.name,self.last_name,self.email,secret_password.hexdigest(),time]
        )
    def user_identify(self):

        secret_password = hashlib.sha256()
        secret_password.update(self.password.encode('utf8'))

        user_identified = self.conection.consult_user(
            [self.email, secret_password.hexdigest()]
        )
        if user_identified == None:
            print("este email y contraseña no se encuentran registrados")
            exit()
        else:
            print(f"Login Realizado de {user_identified[3]}, fecha: {datetime.now()}")
            return user_identified
