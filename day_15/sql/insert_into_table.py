# import mysql.connector
import mysql.connector

#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()
# execute the Query
mycursor.execute("Insert into my_db.test_table values (1,'2024-02-26 10:01:01','sharmi')")
mycursor.execute("Insert into my_db.test_table values (2,'2024-02-26 10:15:11','riu')") 
mycursor.execute("Insert into my_db.test_table values (3,'2024-02-26 10:20:40','rivu')") 
mycursor.execute("Insert into my_db.test_table values (4,'2024-02-26 10:25:01','dipa')") 
mycursor.execute("Insert into my_db.test_table values (5,'2024-02-26 10:30:31','riya')") 
mycursor.execute("Insert into my_db.test_table values (6,'2024-02-26 10:40:12','pijush')") 
mycursor.execute("Insert into my_db.test_table values (7,'2024-02-26 10:50:30','rajesh')") 
mycursor.execute("Insert into my_db.test_table values (8,'2024-02-26 10:55:50','nilu')") 
mycursor.execute("Insert into my_db.test_table values (9,'2024-02-26 10:58:06','surya')") 

mydb.commit() #make the changes permanent
mydb.close()