import psycopg2

class ConectDatabase:
    
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.conn = psycopg2.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

    def insert_user(self,values:list,):

        cur = self.conn.cursor()
        query = 'INSERT INTO "tblUsuario" ("Nombre","Apellido","Email","Contraseña","FechaAuditoria")VALUES (%s,%s,%s,%s,%s);'
        
        try:
            cur.execute(query,values)
            self.conn.commit()
            print("Registro Completado :)")
        except psycopg2.errors.UniqueViolation:
            print("El correo que intentas ingresar ya pertenece a un usuario")

        
    
    def consult_user(self,values:list):

        cur = self.conn.cursor()
        query = 'SELECT * FROM "tblUsuario" WHERE "Email" = %s AND "Contraseña" = %s'
   
        cur.execute(query,values)
        result = cur.fetchone()
          
        self.conn.commit()
        

        return result
    
    def insert_note(self,values:list):
        
        cur = self.conn.cursor()
        query = 'INSERT INTO "tblNota" ("IdUsuario","TituloNota","Contenido","FechaAuditoria") VALUES (%s,%s,%s,%s)'

        cur.execute(query,values)
        print("Nota Agregada :)")

        self.conn.commit()
        

    def consult_notes(self,values:str):

        cur = self.conn.cursor()
        query = 'SELECT * FROM "tblNota" where "IdUsuario" = %s '

        cur.execute(query,values)
        result = cur.fetchall()

        self.conn.commit()
        

        return result

    def delete_notes(self,values:list):

        # cur = self.conn.cursor()
        cursor_execute = self.conn.cursor()
        query = 'DELETE FROM "tblNota" WHERE "IdUsuario" = %s AND "TituloNota" = %s'

        cursor_execute.execute(query,values)
        print("Nota eliminada")

        self.conn.commit()
        
    def close_conection(self):
        self.conn.close()