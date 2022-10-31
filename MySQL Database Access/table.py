import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="name",
  password="pw",
  database="dbname"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
