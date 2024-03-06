import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="karthik'sSQL",
    password="9177765499.",
    database="mydatabase"
)

mycursor = mydb.cursor()
print("something")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
