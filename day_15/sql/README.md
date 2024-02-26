# lab-python-mysql


<!-- ![image](https://user-images.githubusercontent.com/115451707/196919992-edcfea8b-e3f6-4f35-9398-43be66b5622d.png) -->


### MYSQL  Credential

```
user_name: abc
password: password
```

To connect with mysql using extension mysql

![image](https://user-images.githubusercontent.com/115451707/197224168-9179e4b7-22d9-4caa-8b84-d5db4c325412.png)

![image](https://user-images.githubusercontent.com/115451707/197224293-51380d3e-7677-4877-8a05-86582d8e52e0.png)
![image](https://user-images.githubusercontent.com/115451707/197224903-78886c70-9a06-4138-a171-4b3a828e3913.png)
![image](https://user-images.githubusercontent.com/115451707/197224988-72e00ff7-8a37-42a2-a7ed-d654038a2f82.png)
![image](https://user-images.githubusercontent.com/115451707/197225204-2ad0a73b-3a25-4265-b880-198c9043aa1e.png)
![image](https://user-images.githubusercontent.com/115451707/197225690-0e87580d-37de-4f3a-8efe-c7aa207d2e9d.png)
![image](https://user-images.githubusercontent.com/115451707/197225889-46c66e22-8597-4c93-b5d9-cb4f3166560d.png)

Hurrey You have successfully connect with mysql


To connect with mysql in terminal

Launch a terminal
![image](https://user-images.githubusercontent.com/115451707/197226245-a1261158-9ad9-41e8-9b09-19dde495ac95.png)

![image](https://user-images.githubusercontent.com/115451707/197226486-ea785a81-035d-412d-b6ba-20da008d9e26.png)

![image](https://user-images.githubusercontent.com/115451707/197226861-16fbf655-0f68-4f2e-a5cb-6c6d8e1244c9.png)


Let's connect mysql with python code

first again launch a new terminal.

execute below command
```
pip install mysql-connector-python
```

Create a file "demo.py" and paste the below snippet
```
import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
```

Now run the script
```
python demo.py
```