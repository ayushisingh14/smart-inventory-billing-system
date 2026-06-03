#Database Connection Settings
import psycopg2


def connection():
    con = psycopg2.connect(
        host="localhost",
        database="ecommerce",
        user="postgres",
        password="YOUR_PASSWORD_HERE", # Users: replace this with your postgres password
        port="5432"
    )

    if con:
        print("Connection successful")
    else:
        print("Connection failed")
    return con
conn = connection() 