# import mysql.connector
import mysql.connector

#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
# execute the Query
mycursor.execute("SELECT * from my_db.test_table")
mydb.close()
