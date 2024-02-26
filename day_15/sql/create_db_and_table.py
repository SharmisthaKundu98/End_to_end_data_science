# import mysql.connector
import mysql.connector

#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE if not EXISTS my_db2")

mycursor.execute("CREATE TABLE if NOT exists my_db2.test_table( \
        test_id INT NOT NULL PRIMARY KEY,\
        test_time DATETIME COMMENT 'Create Time',\
        test_name VARCHAR(100))")

# close the connection
mydb.close()