from Users.actions import Action
from Users.user import User
from Notes.notes import Notes

'''
Proyecto:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bd
- Si elegimos login, identifica al usuario y pregunta:
    - crear nota
    - borrar nota
    - mostrar nota
'''
def home ():

    print("""
Acciones disponibles:
    - registro
    - login
    - salir
    """)

    option = str(input("Que quieres hacer:"))
    return option

request = home()

while request != "registro" and request != "login" and request != "salir":
    print("Comando equivocado, aqui vamos de nuevo")
    request = str(input("Que quieres hacer:"))

action = Action()

while request != "salir":

    if request == "registro":
        list_register = action.register()

        load_register = User(
            name = list_register["name"],
            last_name = list_register["last_name"],
            email = list_register["email"],
            password = list_register["password"],
            host = "localhost",
            user = "postgres",
            password_database = "qwer1234",
            database = "notes", 
        )

        load_register.user_register()
        request = home()

    elif request == "login":
        list_login = action.login()

        load_login = User(
            email = list_login["email"],
            password = list_login["password"],
            host = "localhost",
            user = "postgres",
            password_database = "qwer1234",
            database = "notes", 
        )

        user_identified=load_login.user_identify()
        action_notes= action.login_notes(user_identified[1])

        notes = Notes(  
            host = "localhost",
            user = "postgres",
            password_database = "qwer1234",
            database = "notes", 
        )

        while action_notes != "salir":
            
            if action_notes == "crear":
                print("Vamos a crear tu nota :)")
                notes.load_note(
                    user_identified[0],
                    str(input("Dime el titulo de la nota: ")),
                    str(input("Dime el contenido de la nota: "))
                )
                
            elif action_notes == "mostrar":
                print("Ok vamos a mostrar tus notas")
                print(notes.view_note(user_identified[0]))

            elif action_notes == "eliminar":
                print("Ok vamos a eliminar tus notas")
                notes.delete_note(
                    user_identified[0]
                ) 
            action_notes= action.login_notes(user_identified[1])
        request = home()


print("Saliendo del programa, nos vemos luego!!")