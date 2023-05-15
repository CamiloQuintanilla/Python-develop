import sqlite3

conect = sqlite3.connect('dbconection.db')

cursor = conect.cursor()

#creacion table
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR (255),           
    descripcion TEXT,
    precio  int
)""")
conect.commit()

#insertar datos
# cursor.execute("""
# INSERT INTO productos VALUES 
# (NULL,'PRODUCTO 1','CARACTERISTICAS PRODUCTO',122),
# (NULL,'PRODUCTO 2','CARACTERISTICAS PRODUCTO',122),
# (NULL,'PRODUCTO 3','CARACTERISTICAS PRODUCTO',122),
# (NULL,'PRODUCTO 4','CARACTERISTICAS PRODUCTO',122),
# (NULL,'PRODUCTO 5','CARACTERISTICAS PRODUCTO',122),
# (NULL,'PRODUCTO 6','CARACTERISTICAS PRODUCTO',122)
# """)
# conect.commit()

#consultar datos
cursor.execute("""
SELECT * FROM productos;    
""")
list_products = cursor.fetchall()

for product in list_products:
    print(product)

conect.close()