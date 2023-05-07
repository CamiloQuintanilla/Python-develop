'''
crear una lista con el contenido de esta tabla:

ACCION      AVENTURA            DEPORTES
GTA         ASSESING            FIFA
COD         CRASH               PRO 21
PUBG        PRINCE OF PERSIA    MOTO GP

MOSTRAR INFO ORDENADA   
'''

table = [
    {
        "Categoria":"ACCION",
        "Juegos":[
            "GTA",
            "COD",
            "PUBG"
        ]
    },
    {
        "Categoria":"AVENTURA",
        "Juegos":[
            "ASSESING",
            "CRASH",
            "PRINCE OF PERSIA"
        ]
    },
    {
        "Categoria":"DEPORTES",
        "Juegos":[
            "FIFA",
            "PRO 21",
            "MOTO GP"
        ]
    }
]

for dictionary in table:
    print(f'--------Categoria {dictionary["Categoria"]}----------')
    for game in dictionary['Juegos']:
        print(game)