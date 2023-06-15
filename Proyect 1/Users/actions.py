
class Action:

    def register(self):
        print("OK! Empezare a registrarte en el sistema")
        name = str(input("ingresa tu nombre:"))
        last_name = str(input("ingresa tu apellido:"))
        email = str(input("ingresa tu email:"))
        password = str(input("ingresa tu contraseña:"))

        return {"name":name,"last_name":last_name,"email":email,"password":password}

    def login(self):
        print("Identificate")
        email = str(input("ingresa tu email:"))
        password = str(input("ingresa tu contraseña:"))

        return {"email":email,"password":password}
    
    def login_notes (self,user):
        print(f""" Welcome {user} :)
- Crear nota (crear)
- Mostrar nota (mostrar)
- Eliminar nota (eliminar)
- Salir (salir)
    """)
        action = str(input("Que quieres hacer:"))

        while action != "crear" and action !="mostrar" and action !="eliminar" and action !="salir":
            print("Comando equivocado :(, aqui vamos de nuevo")
            action = str(input("Que quieres hacer:"))
        return action
