import mysql.connector
import psycopg2

HOST = "localhost"
USER = "postgres"
PASSWORD = "qwer1234"
DATABASE = "postgres"

# mysql.connector.connect(
#     host = HOST,
#     user = USER,
#     password = PASSWORD
# )

conn = psycopg2.connect(
    host = HOST,
    user = USER,
    password = PASSWORD  
)