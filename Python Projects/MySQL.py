import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root@01060744077",
)

mycursor = mydb.cursor()



y = str(input())
mycursor.execute("use work")
mycursor.execute("select answer from ai"+" where question = '" + y + "'" )
for x in mycursor:
  print(x)

