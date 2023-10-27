import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user= 'root',
    passwd= 'p$1234567'
)

##create the database
cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE budget")

print("database created")

