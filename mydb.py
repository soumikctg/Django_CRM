import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user='root',
    password='1234'
)

#prepare a cursor obect

cursorObject = dataBase.cursor()

# create a database

cursorObject.execute("CREATE DATABASE CRM")

print("All Done!")